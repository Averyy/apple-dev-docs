# TN3212: Adopting gesture recognizers for Sidecar touch support

**Framework**: Technotes

Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.

#### Overview

In macOS 27, AppKit continues to standardize on gesture recognizers as the primary mechanism for input handling. This change directly affects Sidecar because gesture recognizers are the only way to respond to touch input from a Sidecar-connected iPad running iPadOS 27. If your app relies on tracking loops for mouse event handling, migrate to gesture recognizers to support Sidecar touch input.

This article explains how the gesture recognizer model works, how to implement gesture recognizers correctly for Sidecar touch input, how to update your existing event-handling code, and which APIs macOS 27 adds. Codebases that implement [`nextEvent(matching:)`](https://developer.apple.com/documentation/AppKit/NSWindow/nextEvent(matching:)) or [`mouseDown(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/mouseDown(with:)), [`mouseDragged(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/mouseDragged(with:)), and [`mouseUp(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/mouseUp(with:)) events are most affected by the updates discussed.

#### Understand How Gesture Recognizers Gather Events

In the traditional AppKit responder-based model, mouse event handling was relatively insensitive to the z-ordering of sibling views. As long as a view called through to the superclass’s `mouseDown(with:)` implementation, the event passed through to any hit-testable underlapped sibling. This conveyance through the responder chain effectively bypassed normal hit testing, which wouldn’t consider the underlapped sibling or its descendants.

Gesture recognizers work differently. They don’t follow the responder event chain. Instead, AppKit gathers all possible gesture recognizers at mouse-down or touch-began, using a strict walk of the view hierarchy from the hit-tested top-most view among siblings up to the window. From that point, the gathered set of recognizers all receive the stream of events until the end of the event sequence. This has a few important implications:

- If your view is covered by another, often transparent, view, your gesture recognizer won’t be triggered. This is a common source of confusion when first working with gesture recognizers.
- You can’t place views on top of standard framework controls, because those controls now use gesture recognizers internally. The overlapping view prevents those recognizers from activating. If necessary, rearrange the siblings, or override the occluding view’s [`hitTest(_:)`](https://developer.apple.com/documentation/AppKit/NSView/hitTest(_:)) method and return `nil` to ensure it doesn’t block events going to underlying controls.
- Gesture recognizers can only be added to views. If you want your view controller to handle touch events, add a gesture recognizer to its view and make the view controller the target and delegate.

#### Handle Sidecar Touch Input

Unlike Touch Bar on Mac and touch events in UIKit, gesture recognizers are the only mechanism for receiving direct Sidecar touches. AppKit doesn’t deliver Sidecar touch events through the responder chain or through event monitors.

> **Note**: Local and global event monitors don’t receive touch events. Touch events don’t go through [`NSApp`](https://developer.apple.com/documentation/AppKit/NSApp) or [`sendEvent(_:)`](https://developer.apple.com/documentation/AppKit/NSWindow/sendEvent(_:)).

For touch recognizers that need to yield to scrolling, set the [`isCancellableByScrollGesture`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/isCancellableByScrollGesture) property to `true`.

#### Update Your Event Handling Code

The transition to gesture recognizers on [`NSControl`](https://developer.apple.com/documentation/AppKit/NSControl) objects changes the timing of when AppKit delivers control action messages with respect to event processing. As a result, [`currentEvent`](https://developer.apple.com/documentation/AppKit/NSApplication/currentEvent) no longer returns the event that triggered an action. Use the [`modifierFlags`](https://developer.apple.com/documentation/AppKit/NSEvent/modifierFlags-swift.type.property) and [`pressedMouseButtons`](https://developer.apple.com/documentation/AppKit/NSEvent/pressedMouseButtons) class properties on [`NSEvent`](https://developer.apple.com/documentation/AppKit/NSEvent) instead. Note that a touch is not part of `pressedMouseButtons`.

AppKit still handles keyboard and scroll-wheel events through the responder chain. Hovering via [`mouseMoved(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/mouseMoved(with:)) is still managed with [`NSTrackingArea`](https://developer.apple.com/documentation/AppKit/NSTrackingArea).

#### Implement Custom Gesture Recognizers

AppKit provides a number of existing gesture recognizers: [`NSClickGestureRecognizer`](https://developer.apple.com/documentation/AppKit/NSClickGestureRecognizer), [`NSPressGestureRecognizer`](https://developer.apple.com/documentation/AppKit/NSPressGestureRecognizer), [`NSPanGestureRecognizer`](https://developer.apple.com/documentation/AppKit/NSPanGestureRecognizer), [`NSMagnificationGestureRecognizer`](https://developer.apple.com/documentation/AppKit/NSMagnificationGestureRecognizer), and [`NSRotationGestureRecognizer`](https://developer.apple.com/documentation/AppKit/NSRotationGestureRecognizer). If these recognizers don’t provide the functionality you need, subclass them or create your own custom [`NSGestureRecognizer`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer) subclass. Prefer the built in recognizers when possible.

When you implement a custom `NSGestureRecognizer` subclass, keep the following guidelines in mind:

- Handle cancellation. Implement [`mouseCancelled(with:)`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/mouseCancelled(with:)) and [`touchesCancelled(with:)`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/touchesCancelled(with:)), and set your state to either [`NSGestureRecognizer.State.failed`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/State-swift.enum/failed) or [`NSGestureRecognizer.State.cancelled`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/State-swift.enum/cancelled).
- Use event processing methods only to update internal properties and state, and set your state to [`NSGestureRecognizer.State.began`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/State-swift.enum/began), [`NSGestureRecognizer.State.changed`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/State-swift.enum/changed), or [`NSGestureRecognizer.State.ended`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/State-swift.enum/ended).
- Respond to the input from custom recognizers in action method messages.
- If you need the originating `NSEvent` or [`NSTouch`](https://developer.apple.com/documentation/AppKit/NSTouch) objects, cache them during event processing method callbacks and retrieve the cached objects during the action message.
- End your active gesture recognizer by transitioning to `ended`, `failed`, or `cancelled`. If you don’t, recognizers are blocked from activating.

#### Filter Gesture Recognizer Candidates

Remove inapplicable gesture recognizers during gesture gathering. Gesture recognizers handle this themselves in certain situations, but in many cases only your app knows whether a recognizer applies at the moment of mouse-down or touch-began. Use the following delegate methods, which provide the initiating event when the recognizer itself normally doesn’t:

```swift
// Only called for mouse events.
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
    shouldAttemptToRecognizeWith event: NSEvent) -> Bool

// Only called for touch events.
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
    shouldReceive touch: NSTouch) -> Bool
```

#### Maintain Compatibility with Existing Code

##### Handle Tracking Loop Compatibility

If you subclass an AppKit control and override any of the left-mouse responder methods, that control falls back to a tracking loop path for compatibility. For use cases that require overriding defaults in AppKit, use [`NSControl`](https://developer.apple.com/documentation/AppKit/NSControl) events to make your app compatible with gesture recognizers.

For container views such as [`NSTableView`](https://developer.apple.com/documentation/AppKit/NSTableView) and [`NSCollectionView`](https://developer.apple.com/documentation/AppKit/NSCollectionView), similar tracking loop fallback paths exist. For `NSTableView`, use table view delegate methods such as [`tableView(_:shouldSelectRow:)`](https://developer.apple.com/documentation/AppKit/NSTableViewDelegate/tableView(_:shouldSelectRow:)). For `NSCollectionView`, use collection view delegate methods instead of overriding responder methods.

##### Update to Gesture Recognizer Behavior

If your app depends on sequential, modal interactions that tracking loops provide, AppKit preserves that behavior and provides a way to opt out when you’re ready.

For maximum compatibility, AppKit restricts gesture activations to a single view hierarchy at a time. Unlike in iOS, the person can’t perform multiple interactions simultaneously, though scrolling is a notable exception. This more closely simulates the implicit modality of tracking loops.

You can change this behavior on a per-view basis (child views inherit the setting from their ancestors) via the [`exclusiveGestureBehavior`](https://developer.apple.com/documentation/AppKit/NSView/exclusiveGestureBehavior-swift.property) property on [`NSView`](https://developer.apple.com/documentation/AppKit/NSView). Alternatively, set the default exclusive behavior for your app via the [`NSViewGestureRecognizerIsExclusive`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSViewGestureRecognizerIsExclusive) application information property list entry.

#### Support Third Party Ui Frameworks

If your app embeds a third-party UI framework that doesn’t yet support native touch input, AppKit provides automatic mouse emulation to help bridge the gap.

- A tap emulates a mouse-down followed immediately by a mouse-up.
- A touch and immediate pan emulates trackpad scroll events, even if the UI doesn’t respond to them.
- A long press without movement emulates a [`rightMouseDown(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/rightMouseDown(with:)) (optionally followed by [`rightMouseDragged(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/rightMouseDragged(with:))) with a [`rightMouseUp(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/rightMouseUp(with:)) on touch lift.
- A two-finger pinch or rotation simultaneously emulates both the trackpad magnify and rotate gestures.

As you adopt a touch-native version of the framework, add  [`NSIsTouchNative`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSIsTouchNative) to your application information property list to disable the extra mouse emulation.

#### Explore Updated Apis in Macos 27

macOS 27 adds and updates APIs for touch capabilities, handling control events, configuring scroll behavior, and working with text and dragging that you can use when migrating from tracking loops to gesture recognizers or when polishing your app’s Sidecar behavior.

##### Detect Touch Capability

To determine whether a screen has touch capability, check the [`multiTouch`](https://developer.apple.com/documentation/AppKit/NSScreen/TouchCapabilities-swift.struct/multiTouch) property on [`NSScreen.TouchCapabilities`](https://developer.apple.com/documentation/AppKit/NSScreen/TouchCapabilities-swift.struct).

In macOS 27, this call returns `true` for all displays when a touch-capable Sidecar display is connected, not just for the Sidecar display. In most cases, instead of checking it directly, it’s better to handle events regardless of input source and decide on an alternate presentation based on the interaction type, if needed.

##### Handle Control Events

Several new event types are available in [`NSControl.Events`](https://developer.apple.com/documentation/AppKit/NSControl/Events):

- [`trackingRepeated`](https://developer.apple.com/documentation/AppKit/NSControl/Events/trackingRepeated): An event when multiple `mouseDown(with:)` events with a click count greater than 1 occur.
- [`valueChanged`](https://developer.apple.com/documentation/AppKit/NSControl/Events/valueChanged): An event when the value changes on continuous controls, such as sliders.
- [`primaryActionTriggered`](https://developer.apple.com/documentation/AppKit/NSControl/Events/primaryActionTriggered): An event when a semantic primary action is triggered.
- [`menuActionTriggered`](https://developer.apple.com/documentation/AppKit/NSControl/Events/menuActionTriggered): An event that triggers when a menu gesture occurs, but before the menu presents.
- [`applicationReserved`](https://developer.apple.com/documentation/AppKit/NSControl/Events/applicationReserved): An event with a range of values, allowing your app to define custom control events.

##### Configure Scroll Behavior

[`NSScrollView`](https://developer.apple.com/documentation/AppKit/NSScrollView) now supports pull-to-refresh functionality. See [`NSRefreshController`](https://developer.apple.com/documentation/AppKit/NSRefreshController) for details.

The following new properties let you fine-tune scrolling behavior:

**NSScrollView**

- [`isTouchScrollingEnabled`](https://developer.apple.com/documentation/AppKit/NSScrollView/isTouchScrollingEnabled)
- [`minimumNumberOfTouchesForScrolling`](https://developer.apple.com/documentation/AppKit/NSScrollView/minimumNumberOfTouchesForScrolling)
- [`maximumNumberOfTouchesForScrolling`](https://developer.apple.com/documentation/AppKit/NSScrollView/maximumNumberOfTouchesForScrolling)
- [`scrollGestureForRelationships`](https://developer.apple.com/documentation/AppKit/NSScrollView/scrollGestureForRelationships)

**NSPanGestureRecognizer**

- [`minimumNumberOfTouches`](https://developer.apple.com/documentation/AppKit/NSPanGestureRecognizer/minimumNumberOfTouches) and [`maximumNumberOfTouches`](https://developer.apple.com/documentation/AppKit/NSPanGestureRecognizer/maximumNumberOfTouches): These two properties replace [`numberOfTouchesRequired`](https://developer.apple.com/documentation/AppKit/NSPanGestureRecognizer/numberOfTouchesRequired). Set `maximumNumberOfTouches` to `0` to require exactly `minimumNumberOfTouches` touches; the default value for `maximumNumberOfTouches` is [`NSIntegerMax`](https://developer.apple.com/documentation/ObjectiveC/NSIntegerMax).

**NSGestureRecognizer**

- `isCancellableByScrollGesture`

##### Work with Text and Dragging

[`NSTextSelectionManager`](https://developer.apple.com/documentation/AppKit/NSTextSelectionManager) allows custom text engines to support standard text gestures.

[`NSDraggingSession`](https://developer.apple.com/documentation/AppKit/NSDraggingSession) gains new APIs for better interoperation with gesture recognizers. Use [`beginDraggingSession(items:gesture:source:)`](https://developer.apple.com/documentation/AppKit/NSView/beginDraggingSession(items:gesture:source:)) to start a drag from a gesture recognizer.

macOS 27 also adds gesture-based dragging support for [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) and improved dragging support in [`NSBrowser`](https://developer.apple.com/documentation/AppKit/NSBrowser).

##### Handle Deprecations and Behavior Changes

In apps built with the macOS 27 SDK and Xcode 27, [`location(in:)`](https://developer.apple.com/documentation/AppKit/NSGestureRecognizer/location(in:)) on `NSGestureRecognizer` returns [`NSZeroPoint`](https://developer.apple.com/documentation/Foundation/NSZeroPoint) and logs an error if the receiver’s class doesn’t override the method. Subclasses of `NSGestureRecognizer` must implement `location(in:)` to report a meaningful location. For support with Xcode 27, see [`Xcode support`](https://developer.apple.comhttps://developer.apple.com/support/xcode/).

Use [`GestureInputKinds`](https://developer.apple.com/documentation/SwiftUI/GestureInputKinds) to limit gestures to specific types of input in SwiftUI.

#### Related

- [`Modernize your AppKit app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2026/289)

#### Revision History

- **2026-06-08** First published.

## See Also

- [TN3210: Optimizing your app for iPhone Mirroring](tn3210-optimizing-your-app-for-iphone-mirroring.md)
  Test your app and improve compatibility with iPhone Mirroring.
- [TN3211: Resolving SwiftUI source incompatibilities for State and ContentBuilder](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder.md)
  Update existing code for two foundational changes in SwiftUI built with Xcode 27.
- [TN3208: Preparing your app’s launch screen to meet App Store requirements](tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.md)
  Understand the launch screen requirement for App Store submission starting in iOS 27 and iPadOS 27.
- [TN3205: Low-latency communication with RDMA over Thunderbolt](tn3205-low-latency-communication-with-rdma-over-thunderbolt.md)
  Learn how to use RDMA over Thunderbolt to enable low-latency communication between clusters of Mac computers.
- [TN3206: Updating Apple Pay certificates](tn3206-updating-apple-pay-certificates.md)
  Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3212-adopting-gesture-recognizers-for-sidecar-touch-support)*