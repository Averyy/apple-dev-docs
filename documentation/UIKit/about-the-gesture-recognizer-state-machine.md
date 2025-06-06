# About the Gesture Recognizer State Machine

**Framework**: UIKit

Learn about the states and transitions of the state machine that underlies gesture recognizers.

#### Overview

Gesture recognizers are driven by a state machine, which UIKit uses to ensure the proper handling of events. The state machine determines several important behaviors:

- Whether a continuous gesture recognizer is allowed to enter the [`UIGestureRecognizer.State.began`](uigesturerecognizer/state-swift.enum/began.md) state
- Whether a discrete gesture recognizer is allowed to enter the [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md) state
- When calls to attached action handlers occur

When implementing a custom gesture recognizer, you must update its state machine at appropriate times. A gesture recognizer always starts in the [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md) state, which indicates that it is ready to start processing events. From that state, discrete and continuous gesture recognizers follow different paths until they reach the [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md), [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md), or [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md) state. A gesture recognizer remains in one of those final states until the current event sequence ends, at which point UIKit resets the gesture recognizer and returns it to the [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md) state.

##### Managing State Transitions for a Discrete Gesture Recognizer

When implementing a discrete gesture recognizer, you change the [`state`](uigesturerecognizer/state-swift.property.md) property to one of two possible values: [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md) or [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md). The following image shows the state diagram for these transitions. When incoming events successfully match your gesture, change the state to [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md). When events do not match your intended gesture, change the state to [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md) as soon as you detect the failure.

![The states of a discrete gesture.](https://docs-assets.developer.apple.com/published/9727ff45763a2d8025ecdb5a2bf93dc4/media-3004409%402x.png)

When your gesture recognizer transitions to the [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md) state, UIKit calls the action methods of any associated target objects. UIKit does not call any action methods when the gesture recognizer transitions to the [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md) state.

For an example of how to implement a discrete gesture recognizer, see [`Implementing a Discrete Gesture Recognizer`](implementing-a-discrete-gesture-recognizer.md).

##### Managing State Transitions for a Continuous Gesture Recognizer

The following image shows the state diagram for a continuous gesture recognizer. The state transitions you make can be broken down into three general phases:

1. The initial event sequence moves the gesture recognizer to the [`UIGestureRecognizer.State.began`](uigesturerecognizer/state-swift.enum/began.md) or [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md) state.
2. Subsequent events move the gesture recognizer to the [`UIGestureRecognizer.State.changed`](uigesturerecognizer/state-swift.enum/changed.md) or [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md) state.
3. A final event moves the gesture recognizer to the [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md) state.

![The states of continuous gesture](https://docs-assets.developer.apple.com/published/86d0d5900211f1645a04880a66ddbc28/media-3004408%402x.png)

When your gesture recognizer is in the [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md) state, if the initial event sequence does not match your gesture, move your gesture recognizer to the [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md) state immediately. UIKit normally permits only one gesture recognizer at a time to notify its client. Moving your custom gesture recognizer to the failed state gives other gesture recognizers an opportunity to handle their gestures.

If the initial event sequence matches your gesture, move your gesture recognizer to the [`UIGestureRecognizer.State.began`](uigesturerecognizer/state-swift.enum/began.md) state. For any subsequent events, repeatedly move your gesture recognizer to the [`UIGestureRecognizer.State.changed`](uigesturerecognizer/state-swift.enum/changed.md) state to indicate that the event information has changed. (Always set the gesture recognizer’s [`state`](uigesturerecognizer/state-swift.property.md) property to [`UIGestureRecognizer.State.changed`](uigesturerecognizer/state-swift.enum/changed.md) for each new event, even if the property is already set to that value. Setting that property triggers calls to the associated action methods.) When an event indicates the successful completion of your gesture, change the state to [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md). However, if an event indicates the unsuccessful completion of your gesture, change the state to [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md).

When your gesture recognizer transitions to the [`UIGestureRecognizer.State.began`](uigesturerecognizer/state-swift.enum/began.md), [`UIGestureRecognizer.State.changed`](uigesturerecognizer/state-swift.enum/changed.md), or [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md) states, UIKit calls the action methods of any associated targets. UIKit does not call any action methods when your gesture recognizer transitions to other states.

For an example of how to implement a continuous gesture recognizer, see [`Implementing a Continuous Gesture Recognizer`](implementing-a-continuous-gesture-recognizer.md).

##### Handling Cancellation

Cancellation of a gesture occurs automatically when the current event sequence is interrupted by a system event, such as an incoming phone call. You can also cancel a gesture programmatically based on event information or on conditions in your app. Cancellation prevents the gesture recognizer from performing tasks that the user didn’t intend.

When the system cancels a gesture, UIKit calls the [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) or [`pressesCancelled(_:with:)`](uigesturerecognizer/pressescancelled(_:with:).md) method of your gesture recognizer. When that happens, move your gesture recognizer to the [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md) state immediately. When you move your gesture recognizer to the [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md) state, UIKit calls the gesture recognizer’s action methods one final time before resetting it.

##### Resetting the Gesture Recognizer State Machine

Implement the [`reset()`](uigesturerecognizer/reset().md) method and use it to return your gesture recognizer to its initial configuration. For example, use this method to return your gesture recognizer’s custom properties to their starting values. Before delivering events in a new event sequence, UIKit calls the [`reset()`](uigesturerecognizer/reset().md) method of every gesture recognizer that received touches or is in the [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md), [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md), or [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md) state. In addition to calling the [`reset()`](uigesturerecognizer/reset().md) method, UIKit automatically changes each gesture recognizer’s [`state`](uigesturerecognizer/state-swift.property.md) property back to [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md) so that it can respond to new event sequences.

## See Also

- [Implementing a Discrete Gesture Recognizer](implementing-a-discrete-gesture-recognizer.md)
  If your gesture involves a specific pattern of events, consider implementing a discrete gesture recognizer for it.
- [Implementing a Continuous Gesture Recognizer](implementing-a-continuous-gesture-recognizer.md)
  For gestures that do not easily match a specific pattern, or when you want to use a gesture recognizer to gather touch input, create a continuous gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/about-the-gesture-recognizer-state-machine)*