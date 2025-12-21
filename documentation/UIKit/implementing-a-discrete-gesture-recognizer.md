# Implementing a discrete gesture recognizer

**Framework**: UIKit

If your gesture involves a specific pattern of events, consider implementing a discrete gesture recognizer for it.

#### Overview

A gesture recognizer remains in the [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md) state until events indicate that your gesture succeeded or failed, at which point you change its state. The advantage of discrete gesture recognizers is that they are simpler to implement because they require fewer state transitions. One disadvantage is that because the state change typically occurs later in the event sequence, recognition can easily be preempted by continuous gestures attached to the same view.

The following image shows a checkmark gesture, which is created by tracing one finger down and to the right and then back up and to the right. Because the gesture follows a specific path, it makes sense to use a discrete gesture recognizer.

![A diagram demonstrating a user performing a checkmark gesture.](https://docs-assets.developer.apple.com/published/48b6fb3bf7411300723929167ccc50b6/implementing-a-discrete-gesture-recognizer-1%402x.png)

##### Defining the Conditions for Success

Before implementing your gesture recognizer code, define the conditions for which recognition should occur. The conditions for matching a checkmark gesture are as follows:

- Only the first finger to touch the screen is tracked. All others are ignored.
- The touch always moves left to right.
- The touch moves downward initially but then changes direction and moves upward.
- The upward stroke ends higher on the screen than the initial touch point.

##### Saving Gesture Related Data

With the conditions defined, add properties to your gesture recognizer to track any needed information. For the checkmark gesture, the gesture recognizer needs to know the starting point of the gesture so that it can compare that point to the final point. It also needs to know whether the user’s finger is moving downward or upward.

The following code shows the first part of a custom `CheckmarkGestureRecognizer` class definition. This class stores the initial touch point and the current phase of the gesture. The class also stores the  [`UITouch`](uitouch.md) object associated with the first finger so that it can ignore any other touches.

```swift
enum CheckmarkPhases {
    case notStarted
    case initialPoint
    case downStroke
    case upStroke
} 
class CheckmarkGestureRecognizer : UIGestureRecognizer {
    var strokePhase : CheckmarkPhases = .notStarted
    var initialTouchPoint : CGPoint = CGPoint.zero
    var trackedTouch : UITouch? = nil
   // Overridden methods to come...
```

##### Processing Touch Events

The following code shows the [`touchesBegan(_:with:)`](uiresponder/touchesbegan(_:with:).md) method, which sets up the initial conditions for recognizing the gesture. The gesture fails immediately if the initial event contains two touches. If there is only one touch, the touch object is saved in the `trackedTouch` property. Because UIKit reuses [`UITouch`](uitouch.md) objects, and therefore overwrites their properties, this method also saves the location of the touch in the `initialTouchPoint` property. After the first touch occurs, any new touches added to the event sequence are ignored.

```swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent) {
   super.touchesBegan(touches, with: event)
   if touches.count != 1 {
      self.state = .failed
   } 
 
   // Capture the first touch and store some information about it.
   if self.trackedTouch == nil {
      self.trackedTouch = touches.first
      self.strokePhase = .initialPoint
      self.initialTouchPoint = (self.trackedTouch?.location(in: self.view))!
   } else {
      // Ignore all but the first touch.
      for touch in touches {
         if touch != self.trackedTouch {
            self.ignore(touch, for: event)
         }
      }
   }
}
```

When touch information changes, UIKit calls the [`touchesMoved(_:with:)`](uiresponder/touchesmoved(_:with:).md) method. The following code shows the implementation of this method for the checkmark gesture. This method verifies that the first touch is the correct one, which it should be because all subsequent touches were ignored. It then looks at the movement of that touch. When the initial movement is down and to the right, this method sets the `strokePhase` property to `downStroke`. When the motion changes direction and starts moving upward, the method changes the stroke phase to `upStroke`. If the gesture deviates from this pattern in any way, the method sets the gesture’s state to failed.

```swift
override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent) {
   super.touchesMoved(touches, with: event)
   let newTouch = touches.first 
   // There should be only the first touch.
   guard newTouch == self.trackedTouch else { 
      self.state = .failed 
      return
   } 
   let newPoint = (newTouch?.location(in: self.view))!
   let previousPoint = (newTouch?.previousLocation(in: self.view))!
   if self.strokePhase == .initialPoint {
      // Make sure the initial movement is down and to the right.
      if newPoint.x >= initialTouchPoint.x && newPoint.y >= initialTouchPoint.y {
         self.strokePhase = .downStroke
      } else {         self.state = .failed
      }
   } else if self.strokePhase == .downStroke {
      // Always keep moving left to right.
      if newPoint.x >= previousPoint.x {
         // If the y direction changes, the gesture is moving up again.
         // Otherwise, the down stroke continues.
         if newPoint.y < previousPoint.y {
            self.strokePhase = .upStroke
         }
      } else {
        // If the new x value is to the left, the gesture fails.
        self.state = .failed
      }
   } else if self.strokePhase == .upStroke {
      // If the new x value is to the left, or the new y value
      // changed directions again, the gesture fails.]
      if newPoint.x < previousPoint.x || newPoint.y > previousPoint.y {
         self.state = .failed
      }
   }
}
```

At the end of the touch sequence, UIKit calls the [`touchesEnded(_:with:)`](uiresponder/touchesended(_:with:).md) method. The following code shows the implementation of this method for the checkmark gesture. If the gesture has not already failed, this method determines whether the gesture was moving upward when it ended and determines whether the final point is higher than the initial point. If both conditions are true, the method sets the state to [`recognized`](uigesturerecognizer/state-swift.enum/recognized.md); otherwise, the gesture fails.

```swift
override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent) {
   super.touchesEnded(touches, with: event) 
   let newTouch = touches.first
   let newPoint = (newTouch?.location(in: self.view))!
   // There should be only the first touch.
   guard newTouch == self.trackedTouch else { 
      self.state = .failed 
      return
   } 
   // If the stroke was moving up and the final point is
   // above the initial point, the gesture succeeds.
   if self.state == .possible && 
         self.strokePhase == .upStroke && 
         newPoint.y < initialTouchPoint.y {
      self.state = .recognized
   } else {
      self.state = .failed
   }
}
```

##### Resetting the Gesture Recognizer

In addition to tracking the touches, the `CheckmarkGestureRecognizer` class implements the [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) and [`reset()`](uigesturerecognizer/reset().md) methods. The class uses these methods to reset the gesture recognizer’s local properties to appropriate values. The following code shows the implementations of these methods.

```swift
override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent) {
   super.touchesCancelled(touches, with: event)
   self.initialTouchPoint = CGPoint.zero
   self.strokePhase = .notStarted
   self.trackedTouch = nil
   self.state = .cancelled
}
 
override func reset() {
   super.reset()
   self.initialTouchPoint = CGPoint.zero
   self.strokePhase = .notStarted
   self.trackedTouch = nil
}
```

## See Also

- [About the Gesture Recognizer State Machine](about-the-gesture-recognizer-state-machine.md)
  Learn about the states and transitions of the state machine that underlies gesture recognizers.
- [Implementing a Continuous Gesture Recognizer](implementing-a-continuous-gesture-recognizer.md)
  For gestures that do not easily match a specific pattern, or when you want to use a gesture recognizer to gather touch input, create a continuous gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/implementing-a-discrete-gesture-recognizer)*