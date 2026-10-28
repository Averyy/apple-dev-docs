# TN3212: Adopting gesture recognizers for Sidecar touch support

**Framework**: Technotes  
**Role**: Technote

Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.

## Overview

In macOS 27, AppKit continues to standardize on gesture recognizers as the primary mechanism for input handling. This change directly affects Sidecar because gesture recognizers are the only way to respond to touch input from a Sidecar-connected iPad running iPadOS 27. If your app relies on tracking loops for mouse event handling, migrate to gesture recognizers to support Sidecar touch input.

This article explains how the gesture recognizer model works, how to implement gesture recognizers correctly for Sidecar touch input, how to update your existing event-handling code, and which APIs macOS 27 adds. Codebases that implement [`nextEvent(matching:)`](../AppKit/nswindow/nextevent%28matching%29.md) or [`mouseDown(with:)`](../AppKit/nsresponder/mousedown%28with%29.md), [`mouseDragged(with:)`](../AppKit/nsresponder/mousedragged%28with%29.md), and [`mouseUp(with:)`](../AppKit/nsresponder/mouseup%28with%29.md) events are most affected by the updates discussed.

## Understand how gesture recognizers gather events

In the traditional AppKit responder-based model, mouse event handling was relatively insensitive to the z-ordering of sibling views. As long as a view called through to the superclass’s `mouseDown(with:)` implementation, the event passed through to any hit-testable underlapped sibling. This conveyance through the responder chain effectively bypassed normal hit testing, which wouldn’t consider the underlapped sibling or its descendants.

Gesture recognizers work differently. They don’t follow the responder event chain. Instead, AppKit gathers all possible gesture recognizers at mouse-down or touch-began, using a strict walk of the view hierarchy from the hit-tested top-most view among siblings up to the window. From that point, the gathered set of recognizers all receive the stream of events until the end of the event sequence. This has a few important implications:

- If your view is covered by another, often transparent, view, your gesture recognizer won’t be triggered. This is a common source of confusion when first working with gesture recognizers.
- You can’t place views on top of standard framework controls, because those controls now use gesture recognizers internally. The overlapping view prevents those recognizers from activating. If necessary, rearrange the siblings, or override the occluding view’s [`hitTest(_:)`](../AppKit/nsview/hittest%28_%29.md) method and return `nil` to ensure it doesn’t block events going to underlying controls.
- Gesture recognizers can only be added to views. If you want your view controller to handle touch events, add a gesture recognizer to its view and make the view controller the target and delegate.

## Handle Sidecar touch input

Unlike Touch Bar on Mac and touch events in UIKit, gesture recognizers are the only mechanism for receiving direct Sidecar touches. AppKit doesn’t deliver Sidecar touch events through the responder chain or through event monitors.

> **Note**: Local and global event monitors don’t receive touch events. Touch events don’t go through [`NSApp`](../AppKit/nsapp.md) or [`sendEvent(_:)`](../AppKit/nswindow/sendevent%28_%29.md).

For touch recognizers that need to yield to scrolling, set the [`isCancellableByScrollGesture`](../AppKit/nsgesturerecognizer/iscancellablebyscrollgesture.md) property to `true`.

## Update your event-handling code

The transition to gesture recognizers on [`NSControl`](../AppKit/nscontrol.md) objects changes the timing of when AppKit delivers control action messages with respect to event processing. As a result, [`currentEvent`](../AppKit/nsapplication/currentevent.md) no longer returns the event that triggered an action. Use the [`modifierFlags`](../AppKit/nsevent/modifierflags-swift.type.property.md) and [`pressedMouseButtons`](../AppKit/nsevent/pressedmousebuttons.md) class properties on [`NSEvent`](../AppKit/nsevent.md) instead. Note that a touch is not part of `pressedMouseButtons`.

AppKit still handles keyboard and scroll-wheel events through the responder chain. Hovering via [`mouseMoved(with:)`](../AppKit/nsresponder/mousemoved%28with%29.md) is still managed with [`NSTrackingArea`](../AppKit/nstrackingarea.md).

## Implement custom gesture recognizers

AppKit provides a number of existing gesture recognizers: [`NSClickGestureRecognizer`](../AppKit/nsclickgesturerecognizer.md), [`NSPressGestureRecognizer`](../AppKit/nspressgesturerecognizer.md), [`NSPanGestureRecognizer`](../AppKit/nspangesturerecognizer.md), [`NSMagnificationGestureRecognizer`](../AppKit/nsmagnificationgesturerecognizer.md), and [`NSRotationGestureRecognizer`](../AppKit/nsrotationgesturerecognizer.md). If these recognizers don’t provide the functionality you need, subclass them or create your own custom [`NSGestureRecognizer`](../AppKit/nsgesturerecognizer.md) subclass. Prefer the built in recognizers when possible.

When you implement a custom `NSGestureRecognizer` subclass, keep the following guidelines in mind:

- Handle cancellation. Implement [`mouseCancelled(with:)`](../AppKit/nsgesturerecognizer/mousecancelled%28with%29.md) and [`touchesCancelled(with:)`](../AppKit/nsgesturerecognizer/touchescancelled%28with%29.md), and set your state to either [`NSGestureRecognizer.State.failed`](../AppKit/nsgesturerecognizer/state-swift.enum/failed.md) or [`NSGestureRecognizer.State.cancelled`](../AppKit/nsgesturerecognizer/state-swift.enum/cancelled.md).
- Use event processing methods only to update internal properties and state, and set your state to [`NSGestureRecognizer.State.began`](../AppKit/nsgesturerecognizer/state-swift.enum/began.md), [`NSGestureRecognizer.State.changed`](../AppKit/nsgesturerecognizer/state-swift.enum/changed.md), or [`NSGestureRecognizer.State.ended`](../AppKit/nsgesturerecognizer/state-swift.enum/ended.md).
- Respond to the input from custom recognizers in action method messages.
- If you need the originating `NSEvent` or [`NSTouch`](../AppKit/nstouch.md) objects, cache them during event processing method callbacks and retrieve the cached objects during the action message.
- End your active gesture recognizer by transitioning to `ended`, `failed`, or `cancelled`. If you don’t, recognizers are blocked from activating.

## Filter gesture recognizer candidates

Remove inapplicable gesture recognizers during gesture gathering. Gesture recognizers handle this themselves in certain situations, but in many cases only your app knows whether a recognizer applies at the moment of mouse-down or touch-began. Use the following delegate methods, which provide the initiating event when the recognizer itself normally doesn’t:

```swift
// Only called for mouse events.
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
    shouldAttemptToRecognizeWith event: NSEvent) -> Bool

// Only called for touch events.
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
    shouldReceive touch: NSTouch) -> Bool
```

## Maintain compatibility with existing code

### Handle tracking loop compatibility

If you subclass an AppKit control and override any of the left-mouse responder methods, that control falls back to a tracking loop path for compatibility. For use cases that require overriding defaults in AppKit, use [`NSControl`](../AppKit/nscontrol.md) events to make your app compatible with gesture recognizers.

For container views such as [`NSTableView`](../AppKit/nstableview.md) and [`NSCollectionView`](../AppKit/nscollectionview.md), similar tracking loop fallback paths exist. For `NSTableView`, use table view delegate methods such as [`tableView(_:shouldSelectRow:)`](../AppKit/nstableviewdelegate/tableview%28_,shouldselectrow%29.md). For `NSCollectionView`, use collection view delegate methods instead of overriding responder methods.

### Update to gesture recognizer behavior

If your app depends on sequential, modal interactions that tracking loops provide, AppKit preserves that behavior and provides a way to opt out when you’re ready.

For maximum compatibility, AppKit restricts gesture activations to a single view hierarchy at a time. Unlike in iOS, the person can’t perform multiple interactions simultaneously, though scrolling is a notable exception. This more closely simulates the implicit modality of tracking loops.

You can change this behavior on a per-view basis (child views inherit the setting from their ancestors) via the [`exclusiveGestureBehavior`](../AppKit/nsview/exclusivegesturebehavior-swift.property.md) property on [`NSView`](../AppKit/nsview.md). Alternatively, set the default exclusive behavior for your app via the [`NSViewGestureRecognizerIsExclusive`](../BundleResources/information-property-list/nsviewgesturerecognizerisexclusive.md) application information property list entry.

## Support third-party UI frameworks

If your app embeds a third-party UI framework that doesn’t yet support native touch input, AppKit provides automatic mouse emulation to help bridge the gap.

- A tap emulates a mouse-down followed immediately by a mouse-up.
- A touch and immediate pan emulates trackpad scroll events, even if the UI doesn’t respond to them.
- A long press without movement emulates a [`rightMouseDown(with:)`](../AppKit/nsresponder/rightmousedown%28with%29.md) (optionally followed by [`rightMouseDragged(with:)`](../AppKit/nsresponder/rightmousedragged%28with%29.md)) with a [`rightMouseUp(with:)`](../AppKit/nsresponder/rightmouseup%28with%29.md) on touch lift.
- A two-finger pinch or rotation simultaneously emulates both the trackpad magnify and rotate gestures.

As you adopt a touch-native version of the framework, add  [`NSIsTouchNative`](../BundleResources/information-property-list/nsistouchnative.md) to your application information property list to disable the extra mouse emulation.

## Explore updated APIs in macOS 27

macOS 27 adds and updates APIs for touch capabilities, handling control events, configuring scroll behavior, and working with text and dragging that you can use when migrating from tracking loops to gesture recognizers or when polishing your app’s Sidecar behavior.

### Detect touch capability

To determine whether a screen has touch capability, check the [`multiTouch`](../AppKit/nsscreen/touchcapabilities-swift.struct/multitouch.md) property on [`NSScreen.TouchCapabilities`](../AppKit/nsscreen/touchcapabilities-swift.struct.md).

In macOS 27, this call returns `true` for all displays when a touch-capable Sidecar display is connected, not just for the Sidecar display. In most cases, instead of checking it directly, it’s better to handle events regardless of input source and decide on an alternate presentation based on the interaction type, if needed.

### Handle control events

Several new event types are available in [`NSControl.Events`](../AppKit/nscontrol/events.md):

- [`trackingRepeated`](../AppKit/nscontrol/events/trackingrepeated.md): An event when multiple `mouseDown(with:)` events with a click count greater than 1 occur.
- [`valueChanged`](../AppKit/nscontrol/events/valuechanged.md): An event when the value changes on continuous controls, such as sliders.
- [`primaryActionTriggered`](../AppKit/nscontrol/events/primaryactiontriggered.md): An event when a semantic primary action is triggered.
- [`menuActionTriggered`](../AppKit/nscontrol/events/menuactiontriggered.md): An event that triggers when a menu gesture occurs, but before the menu presents.
- [`applicationReserved`](../AppKit/nscontrol/events/applicationreserved.md): An event with a range of values, allowing your app to define custom control events.

### Configure scroll behavior

[`NSScrollView`](../AppKit/nsscrollview.md) now supports pull-to-refresh functionality. See [`NSRefreshController`](../AppKit/nsrefreshcontroller.md) for details.

The following new properties let you fine-tune scrolling behavior:

**NSScrollView**

- [`isTouchScrollingEnabled`](../AppKit/nsscrollview/istouchscrollingenabled.md)
- [`minimumNumberOfTouchesForScrolling`](../AppKit/nsscrollview/minimumnumberoftouchesforscrolling.md)
- [`maximumNumberOfTouchesForScrolling`](../AppKit/nsscrollview/maximumnumberoftouchesforscrolling.md)
- [`scrollGestureForRelationships`](../AppKit/nsscrollview/scrollgestureforrelationships.md)

**NSPanGestureRecognizer**

- [`minimumNumberOfTouches`](../AppKit/nspangesturerecognizer/minimumnumberoftouches.md) and [`maximumNumberOfTouches`](../AppKit/nspangesturerecognizer/maximumnumberoftouches.md): These two properties replace [`numberOfTouchesRequired`](../AppKit/nspangesturerecognizer/numberoftouchesrequired.md). Set `maximumNumberOfTouches` to `0` to require exactly `minimumNumberOfTouches` touches; the default value for `maximumNumberOfTouches` is [`NSIntegerMax`](../ObjectiveC/nsintegermax.md).

**NSGestureRecognizer**

- `isCancellableByScrollGesture`

### Work with text and dragging

[`NSTextSelectionManager`](../AppKit/nstextselectionmanager.md) allows custom text engines to support standard text gestures.

[`NSDraggingSession`](../AppKit/nsdraggingsession.md) gains new APIs for better interoperation with gesture recognizers. Use [`beginDraggingSession(items:gesture:source:)`](../AppKit/nsview/begindraggingsession%28items,gesture,source%29.md) to start a drag from a gesture recognizer.

macOS 27 also adds gesture-based dragging support for [`NSColor`](../AppKit/nscolor.md) and improved dragging support in [`NSBrowser`](../AppKit/nsbrowser.md).

### Handle deprecations and behavior changes

In apps built with the macOS 27 SDK and Xcode 27, [`location(in:)`](../AppKit/nsgesturerecognizer/location%28in%29.md) on `NSGestureRecognizer` returns [`NSZeroPoint`](../Foundation/nszeropoint.md) and logs an error if the receiver’s class doesn’t override the method. Subclasses of `NSGestureRecognizer` must implement `location(in:)` to report a meaningful location. For support with Xcode 27, see [Xcode support](https://developer.apple.com/support/xcode/).

Use [`GestureInputKinds`](../SwiftUI/gestureinputkinds.md) to limit gestures to specific types of input in SwiftUI.

## Related

- [Modernize your AppKit app](https://developer.apple.com/videos/play/wwdc2026/289)

## Revision history

- **2026-06-08** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3212-adopting-gesture-recognizers-for-sidecar-touch-support)*