# Handling AppKit gestures

**Framework**: AppKit  
**Role**: Article

Use gesture recognizers to simplify input handling and create a consistent platform experience.

## Overview

Your app can receive input from a pointer, such as a mouse or trackpad, or from direct touches on a Mac with a touch display, and each input type reaches your code through different event-handling methods.

The responder chain only tells you that an event happened — a single [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md) or [`touchesBegan(with:)`](./nsresponder/touchesbegan%28with%29.md) call. Recognizing a gesture, like a click versus a drag, or a single click versus a double click, means tracking a sequence of those raw events yourself. Because the responder chain’s methods are specific to each input type, you’d have to write that tracking logic twice: once for mouse events, and again for touch events. For more information about the responder chain, see [Mouse, Keyboard, and Trackpad](./mouse-keyboard-and-trackpad.md).

A gesture recognizer takes over that tracking for you, as a single reusable object that works the same way regardless of input type. Gesture recognizers also let you coordinate between competing interpretations of the same input — for example, delaying a single click’s action until it’s clear a double click won’t follow.

AppKit provides gesture recognizers for common gestures such as click, pan, and magnify. You can create custom gesture recognizers for more complex interactions, such as a swipe. Every gesture recognizer is either discrete or continuous:

- A *discrete* gesture recognizer, such as [`NSClickGestureRecognizer`](./nsclickgesturerecognizer.md), calls your action method exactly once after it recognizes the gesture.
- A *continuous* gesture recognizer, such as [`NSPanGestureRecognizer`](./nspangesturerecognizer.md), calls your action method repeatedly as the gesture progresses, notifying you each time the gesture’s information changes.

## Configure a gesture recognizer

All gesture recognizers subclass the [`NSGestureRecognizer`](./nsgesturerecognizer.md) abstract base class. AppKit provides several subclasses such as [`NSClickGestureRecognizer`](./nsclickgesturerecognizer.md), [`NSPanGestureRecognizer`](./nspangesturerecognizer.md), [`NSMagnificationGestureRecognizer`](./nsmagnificationgesturerecognizer.md), [`NSRotationGestureRecognizer`](./nsrotationgesturerecognizer.md), and [`NSPressGestureRecognizer`](./nspressgesturerecognizer.md) that recognize common gestures. Prefer one of these standard gesture recognizers over creating a custom gesture recognizer. The standard subclasses in AppKit already handle the low-level event-tracking details correctly across every input type, including the edge cases involving canceled input and Multi-Touch gestures, so you don’t have to reimplement that behavior yourself and risk a gesture recognizer that never reaches a terminal state. If a gesture recognizer doesn’t respond as you expect, see [Diagnose unresponsive gesture recognizers](./handling-appkit-gestures.md#Diagnose-unresponsive-gesture-recognizers).

To configure a gesture recognizer, provide:

- A [`target`](./nsgesturerecognizer/target.md): The object that receives notifications when the gesture recognizer’s state changes.
- An [`action`](./nsgesturerecognizer/action.md): The Objective-C selector the system calls on the target to send each notification.
- Optionally, a [`delegate`](./nsgesturerecognizer/delegate.md): An object that provides the rules the system uses to disambiguate between competing gesture recognizers. Provide a delegate only when you need to customize that behavior.

Then add the gesture recognizer to a view to let the system gather it during hit-testing. You can add more than one gesture recognizer to each view.

The following example creates a click gesture recognizer, sets its target and action, and adds it to a view:

```swift
let clickRecognizer = NSClickGestureRecognizer(target: self, action: #selector(handleClick(_:)))
view.addGestureRecognizer(clickRecognizer)
```

In the same class, implement the action method the recognizer calls:

```swift
@objc func handleClick(_ sender: NSClickGestureRecognizer) {
    // Respond to the recognized click.
}
```

## Track gesture recognizer states

All gesture recognizers begin in the [`possible`](./nsgesturerecognizer/state-swift.enum/possible.md) state and end in a terminal state: [`ended`](./nsgesturerecognizer/state-swift.enum/ended.md), [`failed`](./nsgesturerecognizer/state-swift.enum/failed.md), or [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md).

A gesture recognizer updates its [`state`](./nsgesturerecognizer/state-swift.property.md) property to report progress as it recognizes a person’s gesture. As soon as the gesture recognizer receives enough events to recognize a gesture, it sets its state to [`began`](./nsgesturerecognizer/state-swift.enum/began.md). As the gesture recognizer receives further events, it may repeatedly set its state to [`changed`](./nsgesturerecognizer/state-swift.enum/changed.md) to indicate that it updated its properties. After the gesture reaches completion, the gesture recognizer sets its state to [`ended`](./nsgesturerecognizer/state-swift.enum/ended.md).

The following action method for a continuous gesture recognizer checks [`state`](./nsgesturerecognizer/state-swift.property.md) to decide how to respond at each stage:

```swift
@objc func handlePan(_ sender: NSPanGestureRecognizer) {
    switch sender.state {
    case .began, .changed:
        let translation = sender.translation(in: sender.view)
        // Position content at its starting location plus `translation`.
    case .ended:
        // The gesture completed successfully; keep the change.
        break
    case .cancelled:
        // Revert any changes made during `.began` or `.changed`.
        break
    default:
        break
    }
}
```

Depending on timing, a gesture recognizer sets its state to [`failed`](./nsgesturerecognizer/state-swift.enum/failed.md) or [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md):

- **[`failed`](./nsgesturerecognizer/state-swift.enum/failed.md)**: The state a gesture recognizer uses when the current events don’t match the gesture it’s looking for, before it ever recognizes the gesture. If a gesture recognizer sets this after it already delivered an action, the system automatically converts it to [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md) instead.
- **[`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md)**: The state a gesture recognizer uses when it needs to invalidate a gesture that already delivered an action.

The system calls the [`reset()`](./nsgesturerecognizer/reset%28%29.md) method on gesture recognizers to set them back to the [`possible`](./nsgesturerecognizer/state-swift.enum/possible.md) state for reuse. For more information, see [About the Gesture Recognizer State Machine](../UIKit/about-the-gesture-recognizer-state-machine.md).

## Understand gesture recognizer gathering

When a touch or mouse click lands in your app’s window, the system gathers gesture recognizers associated with that event. It does this by *hit-testing* the initial touch or click to the innermost view that lies under the person’s finger or mouse pointer, and collecting all the gesture recognizers found in that view and all of its superviews. The system sends all future events related to that touch or click to the gathered gesture recognizers.

After all gesture recognizers in the gathered set reach a terminal state, the system calls [`reset()`](./nsgesturerecognizer/reset%28%29.md) on all of them, clearing the set.

If another touch lands in the window before the system clears the previous set, the system again hit-tests that touch — potentially to a different view — and collects all the gesture recognizers in that view and its superviews.

> **Note**: When multiple fingers touch an app’s window, each touch may result in a separate collection of gathered gesture recognizers, or may result in intersecting collections. The system keeps track of which gesture recognizers are associated with each touch.

To ensure the system gathers your gesture recognizers as expected, design your view hierarchy with the following in mind:

- If another view, often a transparent one, covers your view, the system doesn’t gather your gesture recognizer, even though the covering view isn’t visible to the person interacting with your app.
- A view that covers a standard AppKit control, such as [`NSControl`](./nscontrol.md), keeps that control’s built-in gesture recognizers from activating, because the control’s behavior depends on them internally. To keep the control working, put it in front of the covering view, or override the covering view’s [`hitTest(_:)`](./nsview/hittest%28_%29.md) so it returns `nil` for points over the control and lets events reach the control beneath it.
- You can’t attach a gesture recognizer to a view controller directly. Instead, add the recognizer to the controller’s view, and make the controller its target and delegate. Your gesture-handling code then lives with the rest of your screen’s logic, and you don’t need a custom view.

The following example shows how an overlay view can override [`hitTest(_:)`](./nsview/hittest%28_%29.md) to avoid blocking a control underneath it. It returns `nil` only for points over the control, so the overlay still receives events elsewhere:

```swift
override func hitTest(_ point: NSPoint) -> NSView? {
    // Let hit-testing pass through to the control beneath this overlay.
    if controlFrameInSuperview.contains(point) {
        return nil
    }
    return super.hitTest(point)
}
```

Returning `nil` unconditionally makes the overlay unable to receive any events, including its own gesture recognizers.

## Implement a custom gesture recognizer

If AppKit doesn’t provide a gesture recognizer for the gesture your app needs, subclass [`NSGestureRecognizer`](./nsgesturerecognizer.md) directly. For example, AppKit doesn’t provide a standard gesture recognizer for a swipe gesture. To recognize a swipe, create a custom subclass that tracks the direction and speed of a drag. A custom gesture recognizer may implement event-handling methods such as [`mouseDown(with:)`](./nsgesturerecognizer/mousedown%28with%29.md) and [`touchesBegan(with:)`](./nsgesturerecognizer/touchesbegan%28with%29.md) to respond to user input by changing its [`state`](./nsgesturerecognizer/state-swift.property.md) property and updating properties that its [`target`](./nsgesturerecognizer/target.md) can read.

With custom gesture recognizers, AppKit doesn’t set the [`state`](./nsgesturerecognizer/state-swift.property.md) property on your behalf. Your event-handling methods need to move the gesture recognizer to a terminal state:

- When gesture input ends, transition to any terminal state: [`ended`](./nsgesturerecognizer/state-swift.enum/ended.md), [`failed`](./nsgesturerecognizer/state-swift.enum/failed.md), or [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md). If you don’t, other gesture recognizers with a failure requirement on yours hang, waiting for it to resolve, and your app can become unresponsive. For more information, see [Diagnose unresponsive gesture recognizers](./handling-appkit-gestures.md#Diagnose-unresponsive-gesture-recognizers).
- The system can cancel a gesture recognizer for touches or mouse input even after it starts recognizing. For example, when the same touches begin a system-level gesture like [`smartMagnify(with:)`](./nsresponder/smartmagnify%28with%29.md), the system takes over those touches for its own use. When this happens, transition specifically to [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md). Failing to handle this gracefully can lead to interaction errors that are difficult to diagnose.
- If you override one event-handling method for a given input type, override all of the related methods for that type. For touch input, if you override [`touchesBegan(with:)`](./nsgesturerecognizer/touchesbegan%28with%29.md), also override [`touchesMoved(with:)`](./nsgesturerecognizer/touchesmoved%28with%29.md), [`touchesEnded(with:)`](./nsgesturerecognizer/touchesended%28with%29.md), and [`touchesCancelled(with:)`](./nsgesturerecognizer/touchescancelled%28with%29.md). For mouse input, also override the cancellation method, [`mouseCancelled(with:)`](./nsgesturerecognizer/mousecancelled%28with%29.md). Not overriding the cancellation methods can cause gesture recognizers to never reach a terminal state.

The system reuses gesture recognizers, so also override [`reset()`](./nsgesturerecognizer/reset%28%29.md) to clear any state your subclass caches between gestures.

## Prioritize gesture recognizers

The system may call the [`action`](./nsgesturerecognizer/action.md) method on a gesture recognizer’s [`target`](./nsgesturerecognizer/target.md) each time it sets its [`state`](./nsgesturerecognizer/state-swift.property.md). Some gathered gesture recognizers may contradict each other. In that case, establish a failure requirement between them. A *failure requirement* is a relationship where one gesture recognizer can’t recognize its gesture until another fails, and you specify it by returning `true` from the delegate’s [`gestureRecognizer(_:shouldRequireFailureOf:)`](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldrequirefailureof%29.md) or [`gestureRecognizer(_:shouldBeRequiredToFailBy:)`](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldberequiredtofailby%29.md) methods. Use this sparingly, because the recognizer that waits responds more slowly. For example, you can give a single-click [`NSClickGestureRecognizer`](./nsclickgesturerecognizer.md) a failure requirement on a double-click recognizer, so a double click runs only the double-click action. Clicks then feel sluggish, so reserve this for cases where running the single-click action first causes a problem.

To do this, configure the double-click recognizer to require two clicks, then return `true` from the delegate method for the single-click recognizer:

```swift
doubleClickRecognizer.numberOfClicksRequired = 2

func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
    shouldRequireFailureOf otherGestureRecognizer: NSGestureRecognizer) -> Bool {
    gestureRecognizer === singleClickRecognizer && otherGestureRecognizer === doubleClickRecognizer
}
```

For more information, see [Preferring one gesture over another](../UIKit/preferring-one-gesture-over-another.md).

A gesture recognizer that a failure requirement blocks stays in the possible state, and the system doesn’t call its action method. If the blocking gesture recognizer recognizes its gesture, the blocked gesture recognizer fails, and its action method never runs. When the blocking gesture recognizer fails, the blocked gesture recognizer is no longer blocked.

By default, the [`gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)`](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldrecognizesimultaneouslywith%29.md) delegate method returns `false`. The system allows only one gathered gesture recognizer to recognize at a time. You may want to allow multiple gesture recognizers to recognize simultaneously; to enable this, return `true` from the same delegate method. For more information, see [Allowing the simultaneous recognition of multiple gestures](../UIKit/allowing-the-simultaneous-recognition-of-multiple-gestures.md).

## Delay responder events

You can configure gesture recognizers to delay calls to responder-based event-handling methods. This is useful when a view’s default responder-based handling, such as [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md), acts on a click before a gesture recognizer can recognize that same click as a gesture. If you set [`delaysPrimaryMouseButtonEvents`](./nsgesturerecognizer/delaysprimarymousebuttonevents.md) to `true`, the system stores the relevant events until the gesture recognizer fails, then delivers them to the appropriate responders. If the gesture recognizer reaches the [`ended`](./nsgesturerecognizer/state-swift.enum/ended.md) state, the system never delivers the events.

[`NSResponder`](./nsresponder.md) also has low-level touch-handling methods, such as [`touchesBegan(with:)`](./nsresponder/touchesbegan%28with%29.md). These methods don’t have an equivalent delay mechanism, and they apply only to indirect touches from a trackpad. Use gesture recognizers in your app rather than overriding these methods directly. For more information about the responder chain, see [Mouse, Keyboard, and Trackpad](./mouse-keyboard-and-trackpad.md).

## Configure exclusive views

In macOS 27 and later, the initial hit-tested view for a mouse click or touch event becomes an *exclusive view* for gathering gesture recognizers. As long as that set of gathered gesture recognizers remains active, the system doesn’t gather gesture recognizers from any view other than the exclusive view, its superviews, and its subviews. This behavior simulates the presence of a single mouse pointer, even when a person touches a Mac with a touch display with several fingers at once.

Exclusive views are on by default. If your app’s information property list doesn’t include the [NSViewGestureRecognizerIsExclusive](../BundleResources/information-property-list/nsviewgesturerecognizerisexclusive.md) key, the system treats it as `YES`. To turn off exclusive views for the entire app and allow gesture recognizer gathering, set the key to `NO`. Xcode adds the key with a value of `NO` to the information property list of new macOS app projects, so those apps don’t use exclusive views unless you change the value to `YES`.

You may also override this behavior on a view hierarchy by setting a view’s [`exclusiveGestureBehavior`](./nsview/exclusivegesturebehavior-swift.property.md) to [`NSView.ExclusiveGestureBehavior.notExclusive`](./nsview/exclusivegesturebehavior-swift.enum/notexclusive.md). AppKit uses this same technique in the standard Color Panel, where you can adjust multiple sliders — such as red, green, and blue — at the same time instead of one at a time.

## Replace event-tracking loops

Many macOS apps rely on *event-tracking loops* — code that repeatedly calls [`nextEvent(matching:until:inMode:dequeue:)`](./nsapplication/nextevent%28matching,until,inmode,dequeue%29.md), passing in the `.eventTracking` run loop mode, to pull and handle mouse clicks and drags one event at a time. The system gathers and updates gesture recognizers as part of the normal event-dispatch path, but an event-tracking loop pulls events out of that path directly. Events that the loop consumes never reach your gathered gesture recognizers, so a loop and a gesture recognizer can’t both handle the same input. To keep an existing loop and add touch support separately, see [Adopting gesture recognizers in your app](./adopting-gesture-recognizers-in-your-app.md).

For example, replace an event-tracking loop like this one, which tracks a drag by pulling events directly from the queue:

```swift
override func mouseDown(with event: NSEvent) {
    let mask: NSEvent.EventTypeMask = [.leftMouseDragged, .leftMouseUp]
    while let nextEvent = NSApp.nextEvent(matching: mask, until: .distantFuture, inMode: .eventTracking, dequeue: true) {
        if nextEvent.type == .leftMouseUp {
            break
        }
        // Handle the drag using `nextEvent`.
    }
}
```

Replace the event-tracking loop with a pan gesture recognizer:

```swift
let panRecognizer = NSPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
view.addGestureRecognizer(panRecognizer)
```

If your app turned off exclusive views by setting `NSViewGestureRecognizerIsExclusive` to `NO` in its information property list, also set the view’s [`exclusiveGestureBehavior`](./nsview/exclusivegesturebehavior-swift.property.md) to [`NSView.ExclusiveGestureBehavior.exclusive`](./nsview/exclusivegesturebehavior-swift.enum/exclusive.md). This prevents simultaneous gesture recognition with unrelated views, which the loop previously prevented implicitly. Exclusive views are on by default, so you don’t need this line otherwise:

```swift
view.exclusiveGestureBehavior = .exclusive
```

## Diagnose unresponsive gesture recognizers

A gesture recognizer is stuck if it hasn’t reached a terminal state within 2 seconds after the person stops interacting with your app, such as when they release the mouse button or lift their fingers. This applies to every gesture recognizer, but the effect is most noticeable with exclusive views, which apply when your app’s `NSViewGestureRecognizerIsExclusive` key is `YES` or absent from the information property list. A stuck gesture recognizer keeps holding its exclusive view. This blocks the system from gathering any recognizers outside that view’s hierarchy and makes the rest of your app appear unresponsive.

To keep a single stuck gesture recognizer from blocking your app indefinitely, the system automatically transitions it to the [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md) state, allowing gesture gathering to resume normally. If you write a custom gesture recognizer, make sure every event-handling method you override eventually leads it to a terminal state. To detect missing methods, do one of the following:

- Set the `NSGestureRecognizerCrashOnMissingOverrides` key in [`UserDefaults`](../Foundation/userdefaults.md) to `YES`.
- Pass the `-NSGestureRecognizerCrashOnMissingOverrides YES` argument to your app in Xcode.

Always check [`state`](./nsgesturerecognizer/state-swift.property.md) in your action method and handle the canceled case explicitly, because setting `NSGestureRecognizerCrashOnMissingOverrides` doesn’t catch every mistake. It doesn’t detect a gesture recognizer that correctly transitions to [`cancelled`](./nsgesturerecognizer/state-swift.enum/cancelled.md) and sends its action, if the action’s target doesn’t handle the canceled state.

Rather than silently canceling a stuck gesture while debugging your app, make the system crash and generate a diagnostic report instead by:

- Setting the `NSCrashOnStuckGestureTimeout` user default to a small number of seconds, such as `2`.
- Passing the `-NSCrashOnStuckGestureTimeout 2` argument to your app in Xcode.

This makes it easier to find the problem with a stack trace.

> ⚠️ **Warning**: Comment out or remove `NSGestureRecognizerCrashOnMissingOverrides` and `NSCrashOnStuckGestureTimeout` before shipping your app. If you leave either one set in a production build, your app crashes when a gesture recognizer is missing an override or gets stuck, instead of the system canceling the gesture recognizer and resuming gesture gathering. Changes to these user defaults or launch arguments take effect only after you rebuild or relaunch your app.

## Related articles

- [Adopting gesture recognizers in your app](./adopting-gesture-recognizers-in-your-app.md)
  Replace mouse-event overrides and tracking loops with gesture recognizers to support both existing mouse behavior and touch input on a Mac with a touch display.
- [Implementing a custom gesture recognizer](../UIKit/implementing-a-custom-gesture-recognizer.md)
  Discover when and how to build your own gesture recognizers.
- [Implementing a discrete gesture recognizer](../UIKit/implementing-a-discrete-gesture-recognizer.md)
  If your gesture involves a specific pattern of events, consider implementing a discrete gesture recognizer for it.
- [Implementing a Continuous Gesture Recognizer](../UIKit/implementing-a-continuous-gesture-recognizer.md)
  For gestures that do not easily match a specific pattern, or when you want to use a gesture recognizer to gather touch input, create a continuous gesture recognizer.

## See Also

### Gesture handling
- [Adopting gesture recognizers in your app](./adopting-gesture-recognizers-in-your-app.md)
  Replace mouse-event overrides and tracking loops with gesture recognizers to support both existing mouse behavior and touch input on a Mac with a touch display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/handling-appkit-gestures)*