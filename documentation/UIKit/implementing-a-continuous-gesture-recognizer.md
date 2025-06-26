# Implementing a Continuous Gesture Recognizer

**Framework**: UIKit

For gestures that do not easily match a specific pattern, or when you want to use a gesture recognizer to gather touch input, create a continuous gesture recognizer.

#### Overview

A continuous gesture recognizer lets you encapsulate your event-handling logic in one place and reuse that logic in multiple views. Although continuous gesture recognizers require a little more effort to implement the state machine, they also perform tasks that would be difficult with a discrete gesture recognizer, such as capturing free-form input.

The following image shows a free-form gesture whose input you might use to draw paths onscreen. Although you could use a pan gesture recognizer to capture the input, your action method would need to handle all of the phases of the capture process, which would add to its complexity. Using a custom gesture recognizer, you can simplify your code by distributing your logic to various methods of your subclass. Using a custom gesture recognizer also means that you can write your code for capturing the path once and reuse it in multiple views.

![A diagram depicting a user triggering a free-form custom continuous gesture recogniser](https://docs-assets.developer.apple.com/published/1fdeedc953c994dd0c2d52654a50ff94/media-3004411%402x.png)

For a custom gesture recognizer that captures touch input, there are no explicit conditions that trigger a failure of the gesture. Instead, the gesture recognizer captures touch input until the touch sequence ends or is cancelled by the system. While the gesture is ongoing, the gesture recognizer places the touch data into a temporary buffer. Clients of the gesture recognizer use their action method to fetch that buffer and apply it temporarily to the app’s content. For example, a client might use that data to draw the path onscreen. Only when the touch sequence ends successfully would those target objects commit the data permanently to the app’s data structures.

##### Saving Gesture Related Data

A continuous gesture recognizer that tracks touch events needs a way to store that information. You cannot simply store references to the [`UITouch`](uitouch.md) objects that you receive because UIKit reuses those objects and overwrites any old values. Instead, you must define custom data structures to store the touch information you need.

The following code shows the definition of a `StrokeSample` struct, whose purpose is to store the location associated with a touch. In your own implementation, you might add other properties to this struct to store information such as the timestamp or the force of the touch.

```swift
struct StrokeSample {
    let location: CGPoint 
 
    init(location: CGPoint) {
        self.location = location
    }
}
```

The following code shows the partial definition of a `TouchCaptureGesture` class used to capture touch information. This class stores touch data in the `samples` property, which is an array of `StrokeSample` structs. The class also stores the [`UITouch`](uitouch.md) object associated with the first finger so that it can ignore any other touches. The implementation of the [`init(coder:)`](https://developer.apple.com/documentation/Foundation/NSCoding/init(coder:)) method ensures that the `samples` property is initialized properly when loading the gesture recognizer from an Interface Builder file.

```swift
class TouchCaptureGesture: UIGestureRecognizer, NSCoding {
   var trackedTouch: UITouch? = nil
   var samples = [StrokeSample]() 
 
   required init?(coder aDecoder: NSCoder) {
      super.init(target: nil, action: nil) 
 
      self.samples = [StrokeSample]()
   } 
   func encode(with aCoder: NSCoder) { }   
   // Overridden methods to come...
}
```

##### Processing Touch Events

The following code shows the [`touchesBegan(_:with:)`](uiresponder/touchesbegan(_:with:).md) method of the `TouchCaptureGesture` class. The gesture fails immediately if the initial event contains two touches. If there is only one touch, the touch object is saved in the `trackedTouch` property and the custom `addSample` helper method creates a new `StrokeSample` struct with the touch data. After the first touch occurs, any new touches added to the event sequence are ignored.

```swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent) {
   if touches.count != 1 {
      self.state = .failed
   } 
 
   // Capture the first touch and store some information about it.
   if self.trackedTouch == nil {
      if let firstTouch = touches.first {
         self.trackedTouch = firstTouch
         self.addSample(for: firstTouch)
         state = .began
      }
   } else {
      // Ignore all but the first touch.
      for touch in touches {
         if touch != self.trackedTouch {
            self.ignore(touch, for: event)
         }
      }
   }
}
 
func addSample(for touch: UITouch) {
   let newSample = StrokeSample(location: touch.location(in: self.view))
   self.samples.append(newSample)
}
```

The [`touchesMoved(_:with:)`](uiresponder/touchesmoved(_:with:).md) and [`touchesEnded(_:with:)`](uiresponder/touchesended(_:with:).md) methods (shown in the following code) record each new sample and update the gesture recognizer’s state. Setting the state to [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md) is equivalent to setting the state to [`recognized`](uigesturerecognizer/state-swift.enum/recognized.md) and results in a call to the gesture recognizer’s action method.

```swift
override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
   self.addSample(for: touches.first!)
   state = .changed
}
 
override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
   self.addSample(for: touches.first!)
   state = .ended
}
```

##### Resetting the Gesture Recognizer

Always implement the [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) and [`reset()`](uigesturerecognizer/reset().md) methods in your gesture recognizers and use them to perform any cleanup. The following code shows the implementation of these methods for the `TouchCaptureGesture` class. Both methods restore the gesture recognizer’s properties to their initial values.

```swift
override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
   self.samples.removeAll()
   state = .cancelled
} 
 
override func reset() {
   self.samples.removeAll()
   self.trackedTouch = nil
}
```

## See Also

- [About the Gesture Recognizer State Machine](about-the-gesture-recognizer-state-machine.md)
  Learn about the states and transitions of the state machine that underlies gesture recognizers.
- [Implementing a Discrete Gesture Recognizer](implementing-a-discrete-gesture-recognizer.md)
  If your gesture involves a specific pattern of events, consider implementing a discrete gesture recognizer for it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/implementing-a-continuous-gesture-recognizer)*