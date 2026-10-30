# Adopting gesture recognizers in your app

**Framework**: AppKit  
**Role**: Article

Replace mouse-event overrides and tracking loops with gesture recognizers to support both existing mouse behavior and touch input on a Mac with a touch display.

## Overview

Gesture recognizers are a shared input model across AppKit, SwiftUI, and Mac Catalyst, so adopting them in your AppKit code makes your event handling behave consistently regardless of which framework the input passes through. This applies whether someone interacts with your app using a mouse, a Sidecar-connected iPad, or a Mac with a touch display.

A gesture recognizer interprets a sequence of low-level events — mouse clicks, touches, or trackpad gestures — as a single, well-defined interaction, such as a click, a press-and-hold, a pan, a pinch, or a rotation, so you don’t have to track events yourself. Attach a gesture recognizer to a view, and it calls your action method when it recognizes that interaction. AppKit provides a standard recognizer for each of these interactions: [`NSClickGestureRecognizer`](./nsclickgesturerecognizer.md), [`NSPressGestureRecognizer`](./nspressgesturerecognizer.md), [`NSPanGestureRecognizer`](./nspangesturerecognizer.md), [`NSMagnificationGestureRecognizer`](./nsmagnificationgesturerecognizer.md), and [`NSRotationGestureRecognizer`](./nsrotationgesturerecognizer.md). For more information, see [Handling AppKit gestures](./handling-appkit-gestures.md).

If your app relies on tracking loops or overrides like [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md), [`mouseDragged(with:)`](./nsresponder/mousedragged%28with%29.md), and [`mouseUp(with:)`](./nsresponder/mouseup%28with%29.md) for mouse-event handling, migrate to gesture recognizers to support touch input. These existing tracking loops and overrides can still run on a Mac with a touch display or a Sidecar-connected iPad, because AppKit emulates mouse events from a single finger tapping or dragging. Relying on this emulation, however, means you miss out on multi-finger gestures, like pinch and rotate, that gesture recognizers handle.

> 💡 **Tip**: Use Sidecar to test touch input without a Mac that has a touch display. To use [Sidecar](https://support.apple.com/en-us/102597), connect an iPad to your Mac. AppKit then routes touch on its screen the same way it does on a Mac with a touch display.

## Prepare your app for a Mac with a touch display

On a Mac with a touch display, a mouse and trackpad work the same way they do on any other Mac, so the main task is making sure your app also handles touch input. Each approach to handling input behaves differently with touch, as shown below:

| Input handling | Behavior with touch | Next step |
| --- | --- | --- |
| Standard AppKit controls and gesture recognizers | Works with touch, with no changes needed. | Test your app, as described below. |
| [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md) overrides and tracking loops | AppKit emulates a single-finger tap or drag, but supports multi-finger gestures and individual touches only through gesture recognizers. | Replace them with gesture recognizers. For more information, see [Replace common mouse-down overrides](./adopting-gesture-recognizers-in-your-app.md#Replace-common-mouse-down-overrides) and [Replace your custom tracking loops with gesture recognizers](./adopting-gesture-recognizers-in-your-app.md#Replace-your-custom-tracking-loops-with-gesture-recognizers). |
| Subclasses of [`NSButton`](./nsbutton.md), [`NSSlider`](./nsslider.md), and other AppKit views that override mouse-handling methods | AppKit falls back to a tracking loop. | Replace the overrides with target-action pairs for tracking events. For more information, see [Handle tracking-loop compatibility](./adopting-gesture-recognizers-in-your-app.md#Handle-tracking-loop-compatibility). |
| Custom [`NSGestureRecognizer`](./nsgesturerecognizer.md) subclasses | A recognizer that never reaches a terminal state keeps its exclusive view, which can make your app appear unresponsive. | Handle cancellation in the recognizer, and make sure it reaches a terminal state. For more information, see [Write a custom gesture recognizer](./adopting-gesture-recognizers-in-your-app.md#Write-a-custom-gesture-recognizer). |

To test your app, use touch in every window, sheet, and popover, and confirm that:

- Controls respond to a tap, and buttons highlight and activate as expected.
- Dragging a view, selecting text, and scrolling work with one finger.
- Pinch and rotate work where your app supports them.
- Small targets, such as resize grips and grab handles, are easy to hit with a finger.

To find code that needs attention, search your project for [`nextEvent(matching:until:inMode:dequeue:)`](./nsapplication/nextevent%28matching,until,inmode,dequeue%29.md) and [`trackEvents(matching:timeout:mode:handler:)`](./nswindow/trackevents%28matching,timeout,mode,handler%29.md), because tracking loops typically call these methods. Also search for [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md) and [`mouseDragged(with:)`](./nsresponder/mousedragged%28with%29.md) overrides, and for uses of [`currentEvent`](./nsapplication/currentevent.md) in control action methods.

Finally, confirm that your app stays responsive after a touch interaction ends, and that every gesture recognizer action method handles the [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md) state. For more information, see [Diagnose unresponsive gesture recognizers](./handling-appkit-gestures.md#Diagnose-unresponsive-gesture-recognizers).

## Filter gesture recognizer candidates

Mouse events travel through the responder chain, where each view or controller gets a chance to handle an event before AppKit passes it to the next one. Gesture recognizers don’t use the responder chain. Instead, AppKit gathers gesture recognizers differently, which affects how you migrate existing responder-based code. For information about gesture recognizer gathering, see [Handling AppKit gestures](./handling-appkit-gestures.md).

When AppKit gathers gesture recognizers at mouse-down or touch-began, not every recognizer it finds is actually applicable to the interaction — only your app knows that. Gesture recognizers handle this themselves in certain situations, but in many cases you need to remove inapplicable ones from the gathered set yourself. Use [`gestureRecognizer(_:shouldAttemptToRecognizeWith:)`](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldattempttorecognizewith%29.md) to inspect the initiating [`NSEvent`](./nsevent.md) for pointer-based input, such as mouse clicks and trackpad gestures (pan, magnify, and rotate), and [`gestureRecognizer(_:shouldReceive:)`](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldreceive%29.md) to inspect each new [`NSTouch`](./nstouch.md) for touch input. Either method gives you the initial input, something the recognizer doesn’t otherwise expose, and lets you stop the recognizer from handling that event stream or touch.

For example, if your view has a resize grip — a small square in the corner that someone drags to resize it — you can attach the resize gesture recognizer to the whole view instead of creating a separate, tiny view just for the grip. But because the recognizer now covers the entire view, not just the grip, it tries to respond to touches anywhere in it unless you filter it using those delegate methods. In the example below, each delegate method filters by location — it checks whether the touch or click happened inside the grip’s frame (`resizeGripFrame`, in the view’s coordinate space), and returns `true` only to give the gesture recognizer a chance to attempt recognition, not to guarantee it succeeds:

```swift
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
    shouldAttemptToRecognizeWith event: NSEvent) -> Bool {
    guard let view = gestureRecognizer.view else { return false }
    return resizeGripFrame.contains(view.convert(event.locationInWindow, from: nil))
}

func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
    shouldReceive touch: NSTouch) -> Bool {
    guard let view = gestureRecognizer.view else { return false }
    return resizeGripFrame.contains(touch.location(in: view))
}
```

If a custom control expects a touch to land inside its visible area, update it to handle touches that land outside that area. For example, a finger aiming for a small resize grip might land just outside the grip’s visible frame.

You can also decline to attempt a gesture based on where it happens. For example, if a timeline view displays many clips, you don’t need to install a gesture recognizer on every clip. Install one on the timeline instead, and use [`gestureRecognizer(_:shouldAttemptToRecognizeWith:)`](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldattempttorecognizewith%29.md) to hit-test the clip under the event. When there’s a clip, store it so your action method knows which clip the person interacted with. When there isn’t, return `false`, and the gesture recognizer is done for that event stream. In the example below, `clip(at:)` is your own helper that returns the clip at a point in the timeline’s coordinate space:

```swift
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
                       shouldAttemptToRecognizeWith event: NSEvent) -> Bool {
    guard let view = gestureRecognizer.view else { return false }
    activeClip = clip(at: view.convert(event.locationInWindow, from: nil))
    return activeClip != nil
}
```

Direct touches don’t call this method. To filter them, implement [`gestureRecognizer(_:shouldReceive:)`](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldreceive%29.md) instead, as shown above.

Once you’ve filtered which recognizers can attempt to recognize, you can also prioritize between the ones that remain by making one recognizer wait for another to fail. Use this sparingly, because the waiting recognizer responds more slowly. For example, making a single click wait for a double click to fail makes clicks feel sluggish. For more information, see [Prioritize gesture recognizers](./handling-appkit-gestures.md#Prioritize-gesture-recognizers).

## Handle touch input

AppKit emulates mouse events from a single finger tapping or dragging, but it doesn’t deliver direct touches ([`NSTouch`](./nstouch.md)) through the responder chain or through event monitors. Gesture recognizers are the only way to respond to multi-finger gestures or to receive individual touches from a Mac with a touch display or a Sidecar-connected iPad. For more on how gesture recognizers give you one consistent model across these different kinds of input, see [Handling AppKit gestures](./handling-appkit-gestures.md).

In most cases, instead of checking whether a device supports touch, write your event-handling code to work the same way regardless of input source, and decide on alternate presentations based on the interaction type. For example, you might make small drag targets — like resize or grab handles — easier to hit with a finger by expanding their touchable area beyond what’s visible, without changing how they respond to a mouse.

If you do need to determine whether a screen has touch capability, for example to offer a touch-specific option such as capturing a signature on a touch display, check [`touchCapabilities`](./nsscreen/touchcapabilities-swift.property.md):

```swift
if let screen = NSScreen.main, screen.touchCapabilities.contains(.multiTouch) {
    // Offer a touch-specific affordance.
}
```

AppKit doesn’t translate touch swipes for you. If your app currently uses [`trackSwipeEvent(options:dampenAmountThresholdMin:max:usingHandler:)`](./nsevent/trackswipeevent%28options,dampenamountthresholdmin,max,usinghandler%29.md), implement your own swipe handling. For full-page navigation swipes, such as going back and forward, check [`isTouchSwipeNavigationEnabled`](./nsevent/istouchswipenavigationenabled.md) first, because the person can turn off swipe navigation in System Settings.

## Update your event-handling code

Because AppKit routes [`NSControl`](./nscontrol.md) interactions through gesture recognizers instead of the responder chain, the timing of when it delivers control action messages relative to event processing also changes, so [`currentEvent`](./nsapplication/currentevent.md) no longer reliably returns the event that initiated an action. If you were using it to check modifier keys or pressed mouse buttons, use [`modifierFlags`](./nsevent/modifierflags-swift.type.property.md) and [`pressedMouseButtons`](./nsevent/pressedmousebuttons.md) instead. These report the state at the time you query them, not at the time of the original event. A touch doesn’t register in [`pressedMouseButtons`](./nsevent/pressedmousebuttons.md):

**After**:

```swift
if NSEvent.modifierFlags.contains(.shift) {
    // Handle a Shift-click.
}
```

**Before**:

```swift
if let event = NSApplication.shared.currentEvent, event.modifierFlags.contains(.shift) {
    // Handle a Shift-click.
}
```

Keyboard events and scroll-wheel events behave the same on every input source: AppKit delivers them through the responder chain. Hover tracking, which relies on [`mouseMoved(with:)`](./nsresponder/mousemoved%28with%29.md) and [`NSTrackingArea`](./nstrackingarea.md), applies to pointer input only, because a touch display has no hover.

## Replace common mouse-down overrides

Most [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md) overrides do one of two things: mark an item as selected when someone clicks it, or show a menu when someone Control-clicks.

For the first case, marking an item as selected in a table view or collection view, you don’t need to handle the click yourself. AppKit already updates the item’s `isSelected` property when someone selects it, so observe that property instead. Use [`isSelected`](./nscollectionviewitem/isselected.md) for collection view items, or [`isSelected`](./nstablerowview/isselected.md) for table rows. Because this observer also runs when your code changes the selection programmatically, make sure the work in `didSet` is safe in both cases.

**After**:

```swift
override var isSelected: Bool {
    didSet {
        guard isSelected else { return }
        delegate?.itemWasSelected(self)
    }
}
```

**Before**:

```swift
override func mouseDown(with event: NSEvent) {
    isSelected = true
    delegate?.itemWasSelected(self)
}
```

If you need to allow or prevent a selection before it happens, implement [`tableView(_:shouldSelectRow:)`](./nstableviewdelegate/tableview%28_,shouldselectrow%29.md) or [`collectionView(_:shouldSelectItemsAt:)`](./nscollectionviewdelegate/collectionview%28_,shouldselectitemsat%29.md) instead.

For the second case, showing a menu on Control-click, let AppKit present it instead of presenting it from a [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md) override. Override [`menu(for:)`](./nsview/menu%28for%29.md) to return a menu based on where someone clicked, as shown below:

**After**:

```swift
override func menu(for event: NSEvent) -> NSMenu? {
    let location = convert(event.locationInWindow, from: nil)
    return itemView(at: location) != nil ? itemMenu : canvasMenu
}
```

**Before**:

```swift
override func mouseDown(with event: NSEvent) {
    guard event.modifierFlags.contains(.control) else {
        return super.mouseDown(with: event)
    }
    let location = convert(event.locationInWindow, from: nil)
    let menu = itemView(at: location) != nil ? itemMenu : canvasMenu
    NSMenu.popUpContextMenu(menu, with: event, for: self)
}
```

If the menu doesn’t depend on the click, set [`menu`](./nsresponder/menu.md) to give an individual view its own menu, or override [`defaultMenu`](./nsview/defaultmenu.md) to give every instance of the view the same menu.

## Handle tracking-loop compatibility

With tracking loops, after you start interacting with a control (like dragging a slider), nothing else in your app can respond to input until that interaction is finished. AppKit still falls back to this same behavior in certain situations, like when you override a control’s own mouse-handling methods.

For example, if you subclass [`NSButton`](./nsbutton.md) to add a highlight animation when someone presses it, and you override [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md) to start that animation, AppKit treats your override as a replacement for its own click handling, rather than as a side effect, and applies that same fallback to the button instead of dispatching through gesture recognizers.

AppKit decides based on whether your subclass overrides the method, not on what the override does, so the fallback still applies if your override calls `super.mouseDown(with:)`. Overriding [`mouseDragged(with:)`](./nsresponder/mousedragged%28with%29.md) or [`mouseUp(with:)`](./nsresponder/mouseup%28with%29.md) has the same effect.

In macOS 27 and later, instead of overriding a mouse-handling method to add a side effect like this, add a target and action for the matching tracking events in [`NSControl.Events`](./nscontrol/events.md), as shown below. The action methods must be exposed to Objective-C with `@objc`:

```swift
// Highlight the button while someone presses it.
openButton.addTarget(self, action: #selector(showHighlight), for: [.trackingBegan, .trackingEntered])

// Remove the highlight when the press ends, leaves the button, or the system cancels it.
openButton.addTarget(self, action: #selector(hideHighlight), for: [.trackingExited, .trackingEndedInside, .trackingEndedOutside, .trackingCancelled])
```

If you only need to know when the press results in an action — regardless of whether someone used a mouse, trackpad, or touch to produce it — add a target and action for [`primaryActionTriggered`](./nscontrol/events/primaryactiontriggered.md) instead:

```swift
// Respond when someone activates the button, whether by clicking or tapping.
openButton.addTarget(self, action: #selector(openDocument), for: .primaryActionTriggered)
```

Container views fall back to tracking-loop behavior in the same way when you override their mouse-handling methods. If you start a drag from [`mouseDragged(with:)`](./nsresponder/mousedragged%28with%29.md) in an [`NSTableView`](./nstableview.md), [`NSCollectionView`](./nscollectionview.md), [`NSOutlineView`](./nsoutlineview.md), or [`NSBrowser`](./nsbrowser.md), AppKit falls back to a tracking loop for the interaction. Instead, implement the dragging methods in [`NSTableViewDataSource`](./nstableviewdatasource.md), [`NSCollectionViewDelegate`](./nscollectionviewdelegate.md), [`NSOutlineViewDataSource`](./nsoutlineviewdatasource.md), or [`NSBrowserDelegate`](./nsbrowserdelegate.md). For example, in a table view, implement [`tableView(_:pasteboardWriterForRow:)`](./nstableviewdatasource/tableview%28_,pasteboardwriterforrow%29.md) to create a pasteboard item, set its data, and return it.

## Replace your custom tracking loops with gesture recognizers

If your code still relies on an event-tracking loop that retrieves mouse events directly until an interaction ends, replace it with gesture recognizers. These loops typically call [`nextEvent(matching:until:inMode:dequeue:)`](./nsapplication/nextevent%28matching,until,inmode,dequeue%29.md) or [`trackEvents(matching:timeout:mode:handler:)`](./nswindow/trackevents%28matching,timeout,mode,handler%29.md) with the `.eventTracking` run loop mode. For more information, see [Replace event-tracking loops](./handling-appkit-gestures.md#Replace-event-tracking-loops).

For example, if your app has a photo editing view where someone drags a caption around an image, use a pan gesture recognizer instead of a tracking loop, as shown below:

**After**:

```swift
private var startOrigin = CGPoint.zero

func setUpGestureRecognizers() {
    let panRecognizer = NSPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
    addGestureRecognizer(panRecognizer)
}

@objc private func handlePan(_ sender: NSPanGestureRecognizer) {
    switch sender.state {
    case .began:
        startOrigin = captionView.frame.origin
    case .changed:
        let translation = sender.translation(in: self)
        captionView.frame.origin = CGPoint(x: startOrigin.x + translation.x,
                                           y: startOrigin.y + translation.y)
    case .cancelled:
        captionView.frame.origin = startOrigin
    default:
        break
    }
}
```

**Before**:

```swift
override func mouseDown(with event: NSEvent) {
    let start = convert(event.locationInWindow, from: nil)
    let originOffset = CGPoint(x: start.x - captionView.frame.minX,
                               y: start.y - captionView.frame.minY)
    window?.trackEvents(matching: [.leftMouseUp, .leftMouseDragged],
                        timeout: NSEvent.foreverDuration,
                        mode: .eventTracking) { event, stop in
        guard let event else { return }
        if event.type == .leftMouseUp { stop.pointee = true }
        let moved = convert(event.locationInWindow, from: nil)
        captionView.frame.origin = CGPoint(x: moved.x - originOffset.x,
                                           y: moved.y - originOffset.y)
    }
}
```

AppKit calls the action method each time the gesture’s state changes. If the system cancels the gesture, use the `.cancelled` state to undo any changes you’ve made.

If your tracking loop starts a drag-and-drop session, pass the gesture recognizer to [`beginDraggingSession(items:gesture:source:)`](./nsview/begindraggingsession%28items,gesture,source%29.md) instead of the event:

**After**:

```swift
beginDraggingSession(items: [draggingItem], gesture: sender, source: self)
```

**Before**:

```swift
beginDraggingSession(with: [draggingItem], event: event, source: self)
```

If you’d rather keep your tracking loop and only add touch support, see the next section.

## Add touch support to your custom tracking loop

If you have an existing custom tracking loop and want to add touch support without rewriting it, add a touch-only gesture recognizer alongside it. Refactor your tracking loop’s logic into separate functions for each phase (start, continue, end, and cancel), then call those same functions from both the tracking loop and a gesture recognizer scoped to touch only:

**After**:

```swift
// Shared tracking functions, extracted from the loop.
private func startTracking(at location: CGPoint) { /* ... */ }
private func continueTracking(at location: CGPoint) { /* ... */ }
private func endTracking(at location: CGPoint) { /* ... */ }
private func cancelTracking() { /* Undo any changes made since startTracking. */ }

// The tracking loop calls the shared functions, so mouse input still works.
override func mouseDown(with event: NSEvent) {
    startTracking(at: convert(event.locationInWindow, from: nil))

    window?.trackEvents(matching: [.leftMouseUp, .leftMouseDragged],
                        timeout: NSEvent.foreverDuration,
                        mode: .eventTracking) { event, stop in
        guard let event else { return }
        let location = convert(event.locationInWindow, from: nil)

        if event.type == .leftMouseUp {
            endTracking(at: location)
            stop.pointee = true
        } else {
            continueTracking(at: location)
        }
    }
}

// A touch-only gesture recognizer calls the same functions.
func setUpGestureRecognizers() {
    let touchRecognizer = NSPanGestureRecognizer(target: self, action: #selector(handleTouchPan))
    touchRecognizer.buttonMask = 0
    touchRecognizer.allowedTouchTypes = .direct
    addGestureRecognizer(touchRecognizer)
}

@objc func handleTouchPan(_ recognizer: NSPanGestureRecognizer) {
    switch recognizer.state {
    case .began: startTracking(at: recognizer.location(in: self))
    case .changed: continueTracking(at: recognizer.location(in: self))
    case .ended: endTracking(at: recognizer.location(in: self))
    case .cancelled: cancelTracking()
    default: break
    }
}
```

**Before**:

```swift
override func mouseDown(with event: NSEvent) {
    // Tracking logic is written inline in the loop.
    let start = convert(event.locationInWindow, from: nil)
    beginDragging(from: start)

    window?.trackEvents(matching: [.leftMouseUp, .leftMouseDragged],
                        timeout: NSEvent.foreverDuration,
                        mode: .eventTracking) { event, stop in
        guard let event else { return }
        let location = convert(event.locationInWindow, from: nil)

        if event.type == .leftMouseUp {
            finishDragging(at: location)
            stop.pointee = true
        } else {
            updateDragging(to: location)
        }
    }
}
```

As shown above, setting [`buttonMask`](./nspangesturerecognizer/buttonmask.md) to `0` means the gesture recognizer only recognizes touches, not mouse or trackpad input, so your tracking loop keeps handling the mouse and trackpad exactly as before. If you leave `buttonMask` at its default, the recognizer also responds to the primary mouse button. A mouse drag then begins the gesture recognizer, and AppKit doesn’t call your `mouseDown(with:)` override, so the tracking loop doesn’t run. A click that doesn’t move still reaches your tracking loop. Direct touches are already the default for [`allowedTouchTypes`](./nsgesturerecognizer/allowedtouchtypes.md), and setting it to `.direct` states that intent explicitly. This is often the fastest, lowest-risk way to add touch support to code with a tracking loop you’d rather not rewrite all at once.

## Write a custom gesture recognizer

AppKit provides a number of standard gesture recognizers, but if none of them provides the functionality you need, subclass one of them or create your own custom [`NSGestureRecognizer`](./nsgesturerecognizer.md) subclass. Prefer the built-in recognizers when possible.

When you implement a custom [`NSGestureRecognizer`](./nsgesturerecognizer.md) subclass, keep the following guidelines in mind:

- Handle cancellation by implementing [`mouseCancelled(with:)`](./nsgesturerecognizer/mousecancelled%28with%29.md) and [`touchesCancelled(with:)`](./nsgesturerecognizer/touchescancelled%28with%29.md). To learn more, see [Implement a custom gesture recognizer](./handling-appkit-gestures.md#Implement-a-custom-gesture-recognizer).
- In your event-processing methods, such as [`mouseDown(with:)`](./nsgesturerecognizer/mousedown%28with%29.md) or [`touchesBegan(with:)`](./nsgesturerecognizer/touchesbegan%28with%29.md), only update your subclass’s own private tracking properties, and set [`state`](./nsgesturerecognizer/state-swift.property.md) to [`began`](./nsgesturerecognizer/state-swift.enum/began.md), [`changed`](./nsgesturerecognizer/state-swift.enum/changed.md), or [`ended`](./nsgesturerecognizer/state-swift.enum/ended.md) as appropriate.
- Respond to the input from custom recognizers in your action method, not in the event-processing callback.
- If you need the originating [`NSEvent`](./nsevent.md) or [`NSTouch`](./nstouch.md) objects, cache them during event processing and retrieve the cached objects in your action method.
- Override [`reset()`](./nsgesturerecognizer/reset%28%29.md) to clear your cached state, so it doesn’t leak from one gesture into the next.
- Always end an active gesture recognizer by transitioning to [`ended`](./nsgesturerecognizer/state-swift.enum/ended.md), [`failed`](./nsgesturerecognizer/state-swift.enum/failed.md), or [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md). Otherwise, other recognizers can’t activate. For more information, see [Diagnose unresponsive gesture recognizers](./handling-appkit-gestures.md#Diagnose-unresponsive-gesture-recognizers).
- Subclasses are responsible for overriding [`location(in:)`](./nsgesturerecognizer/location%28in%29.md) and returning an appropriate value based on the type of gesture. If you skip this override and build your app with the macOS 27 SDK and later, AppKit returns [`NSZeroPoint`](../Foundation/nszeropoint.md) and logs a console error.

The following example shows the structure of a custom drag-tracking recognizer that applies the guidelines above:

```swift
class DragTrackingRecognizer: NSGestureRecognizer {
    // Cache what your action method needs, like the location (in window coordinates) and the originating event.
    private(set) var trackedLocation: NSPoint = .zero
    private(set) var lastEvent: NSEvent?

    // Update the tracking properties and `state` in one place.
    private func track(_ location: NSPoint, event: NSEvent, state newState: State) {
        trackedLocation = location
        lastEvent = event
        state = newState
    }

    override func mouseDown(with event: NSEvent) {
        // Call `track(_:event:state:)` with `event.locationInWindow` and `.began`.
    }

    override func mouseDragged(with event: NSEvent) {
        // Call `track(_:event:state:)` with `event.locationInWindow` and `.changed`.
    }

    override func mouseUp(with event: NSEvent) {
        // Call `track(_:event:state:)` with `event.locationInWindow` and `.ended`.
    }

    override func mouseCancelled(with event: NSEvent) {
        // Set `state` to `.cancelled`.
    }

    // Implement `touchesBegan`, `touchesMoved`, `touchesEnded`, and `touchesCancelled` the same way, caching the relevant `NSTouch` objects instead of an `NSEvent`.

    override func reset() {
        super.reset()
        trackedLocation = .zero
        lastEvent = nil
    }

    override func location(in view: NSView?) -> NSPoint {
        guard let view else { return trackedLocation }
        return view.convert(trackedLocation, from: nil)
    }
}
```

Set it up like any other gesture recognizer, and read the cached state back in your action method instead of the event-processing methods:

```swift
let recognizer = DragTrackingRecognizer(target: self, action: #selector(handleDrag))
view.addGestureRecognizer(recognizer)

@objc func handleDrag(_ recognizer: DragTrackingRecognizer) {
    let location = recognizer.location(in: view)
    let extendsSelection = recognizer.lastEvent?.modifierFlags.contains(.shift) == true

    switch recognizer.state {
    case .began, .changed:
        moveHandle(to: location, extendingSelection: extendsSelection)
    case .ended:
        commitHandleMove()
    case .cancelled:
        revertHandleMove()
    default:
        break
    }
}
```

For more information, see [Handling AppKit gestures](./handling-appkit-gestures.md).

## Account for gesture recognizer behavior changes

Gesture recognizers replace tracking loops, but AppKit preserves the same one-view-at-a-time behavior that tracking loops implicitly provide, and gives you a way to opt out when you’re ready.

Exclusive views are on by default: while one view’s gesture recognizers are handling an interaction, AppKit won’t gather gesture recognizers from a different part of your view hierarchy until that interaction ends. Xcode adds the [`NSViewGestureRecognizerIsExclusive`](../BundleResources/information-property-list/nsviewgesturerecognizerisexclusive.md) key with a value of `NO` to new macOS app projects, so those apps don’t use exclusive views unless you change the value to `YES`. For the full mechanism, including how to opt out with [`exclusiveGestureBehavior`](./nsview/exclusivegesturebehavior-swift.property.md) or that property list key, see [Configure exclusive views](./handling-appkit-gestures.md#Configure-exclusive-views).

Two properties help your gesture recognizers coexist with a scroll view’s own gestures. Use [`scrollGestureForRelationships`](./nsscrollview/scrollgestureforrelationships.md) when your own recognizers compete with the scroll view’s, and use [`isCancellableByScrollGesture`](./nsgesturerecognizer/iscancellablebyscrollgesture.md) when a control’s recognizer needs to yield to scrolling.

As you migrate, watch for this scenario. When someone touches down on a control (like a button) that sits inside a scroll view, and then drags to scroll or pinches to zoom the content instead of clicking the control, set [`isCancellableByScrollGesture`](./nsgesturerecognizer/iscancellablebyscrollgesture.md) to `true` on the control’s gesture recognizer to let AppKit cancel it once the scroll view’s pan or magnification gesture starts. This means scrolling or zooming takes precedence over the control’s own gesture, the same way it already takes precedence over unrelated exclusive views elsewhere in the hierarchy.

These settings don’t override each other. Each one controls a different part of how AppKit handles gestures:

- [`exclusiveGestureBehavior`](./nsview/exclusivegesturebehavior-swift.property.md) and the [`NSViewGestureRecognizerIsExclusive`](../BundleResources/information-property-list/nsviewgesturerecognizerisexclusive.md) key control whether a view’s gesture recognizers become the exclusive set, which affects which gesture recognizers AppKit gathers. The view’s setting applies to that view and its subviews, and takes precedence over the app-wide key. A view that isn’t exclusive never becomes the exclusive view, but an exclusive view that’s already active still blocks AppKit from gathering gesture recognizers outside its hierarchy until the interaction ends.
- [`isCancellableByScrollGesture`](./nsgesturerecognizer/iscancellablebyscrollgesture.md) applies to an individual gesture recognizer and is independent of exclusivity. It lets a scroll gesture cancel that gesture recognizer even if it has already begun.

For example, a button in a non-exclusive container inside a scroll view still yields to scrolling if its gesture recognizer’s `isCancellableByScrollGesture` is `true`, because exclusivity doesn’t affect that behavior.

Beyond these behavior changes, [`NSScrollView`](./nsscrollview.md) and [`NSPanGestureRecognizer`](./nspangesturerecognizer.md) also provide several touch-related properties, including pull-to-refresh support and control over how many simultaneous touches scroll a view.

Custom text engines that adopt [`NSTextSelectionManager`](./nstextselectionmanager.md) to support standard text-selection gestures run into the same kind of competition. The selection manager creates its gesture recognizers itself, so you don’t have a reference to them. To make your own gesture recognizer wait for them to fail, return `true` from [`gestureRecognizer(_:shouldRequireFailureOf:)`](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldrequirefailureof%29.md) when [`gesturesForFailureRequirements`](./nstextselectionmanager/gesturesforfailurerequirements.md) contains `otherGestureRecognizer`, as shown below:

```swift
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
                       shouldRequireFailureOf otherGestureRecognizer: NSGestureRecognizer) -> Bool {
    gestureRecognizer === myRecognizer
        && selectionManager.gesturesForFailureRequirements.contains(otherGestureRecognizer)
}
```

For more information, see [Prioritize gesture recognizers](./handling-appkit-gestures.md#Prioritize-gesture-recognizers).

## Support non-AppKit UI frameworks

If your app embeds a non-AppKit UI framework that doesn’t yet handle touch input directly, AppKit provides automatic mouse emulation to help bridge the gap:

- Tapping emulates a mouse-down followed immediately by a mouse-up.
- Touching and then immediately panning emulates a trackpad scroll, even if the UI doesn’t otherwise handle Multi-Touch input directly.
- Touching, briefly holding, and then moving emulates [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md), followed by [`mouseDragged(with:)`](./nsresponder/mousedragged%28with%29.md) as it moves, and [`mouseUp(with:)`](./nsresponder/mouseup%28with%29.md) on lift.
- Touching and holding without movement emulates [`rightMouseDown(with:)`](./nsresponder/rightmousedown%28with%29.md), and [`rightMouseUp(with:)`](./nsresponder/rightmouseup%28with%29.md) on lift.
- Pinching or rotating with two fingers emulates the trackpad magnify and rotate gestures.

This emulation covers interactions with one or two fingers. If another finger touches down during a pinch or rotation, the emulation ignores it and keeps tracking the original two fingers. To respond to interactions that involve three or more fingers, use gesture recognizers.

Once the framework adds its own direct touch handling, set the [`NSIsTouchNative`](../BundleResources/information-property-list/nsistouchnative.md) property list key to `YES` to disable the extra mouse emulation.

## Videos

- [Bring Touch to your Mac app](https://developer.apple.com/videos/play/tech-talks/111468)
  Discover how to add touch capabilities to your Mac app. Explore how to transition from classic mouse tracking APIs to modern gesture recognizers and touch-native controls. Find out how to optimize hit targets, implement multi-touch interactions, and manage system gestures to deliver an incredible touch experience. To get the most out of this session, watch Design for Touch on Mac.

## Related articles

- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)
  People rely on the power, spaciousness, and flexibility of a Mac as they perform in-depth productivity tasks, view media or content, and play games, often using several apps at once.
- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
  A gesture is a physical motion that a person uses to directly affect an object in an app or game on their device.
- [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)
  People can use a pointing device like a trackpad or mouse to navigate the interface and initiate actions.
- [TN3216: Supporting touch input for games on macOS](../Technotes/tn3216-supporting-touch-input-for-games-on-macos.md)
  Let players interact with your game through touch on a Mac with a touch display or a Sidecar-connected iPad.
- [TN3212: Adopting gesture recognizers for Sidecar touch support](../Technotes/tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.md)
  Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.

## See Also

### Essentials
- [Adopting Liquid Glass](../TechnologyOverviews/adopting-liquid-glass.md)
  Find out how to bring the new material to your app.
- [AppKit updates](../Updates/appkit.md)
  Learn about important changes to AppKit.
- [Protecting the User’s Privacy](../UIKit/protecting-the-user-s-privacy.md)
  Secure personal data, and respect user preferences for how data is used.
- [Porting your macOS apps to Apple silicon](../apple-silicon/porting-your-macos-apps-to-apple-silicon.md)
  Create a version of your macOS app that runs on both Apple silicon and Intel-based Mac computers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/adopting-gesture-recognizers-in-your-app)*