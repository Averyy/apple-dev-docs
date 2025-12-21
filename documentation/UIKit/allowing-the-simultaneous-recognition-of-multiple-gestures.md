# Allowing the simultaneous recognition of multiple gestures

**Framework**: UIKit

Learn how to use a delegate object to allow detection of more than one gesture at a time.

#### Overview

There are times when it makes sense to allow the simultaneous recognition of multiple gestures. The following image shows an app that allows people to drag, scale, and rotate three views onscreen. Each view maintains its own unique set of pan, pinch, and rotate gesture recognizers, and it’s possible for all three of a view’s gesture recognizers to perform their actions simultaneously.

![A screenshot of an app that demonstrates how a person can use rotation, pinch and pan gestures simultaneously to control the appearance of a pink square.](https://docs-assets.developer.apple.com/published/8559fcb4402d0499f4e131301b8d0e58/media-2880130%402x.png)

To allow a gesture recognizer to operate simultaneously with other gestures, assign a delegate object that implements the [`gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:).md) method to it. UIKit calls this method for pairs of gesture recognizers attached to the same view. Returning `true` allows both gestures to process events simultaneously.

The following code shows the [`gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:).md) method from the app shown in the previous image. This method returns `true` when the gesture recognizers are attached to the same view. If the gesture recognizers are attached to different views, or if one of the objects is a long press gesture recognizer, this method returns `false`.

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer,
       shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer)
        -> Bool {
   // If the gesture recognizer's view isn't one of the squares, do not
   // allow simultaneous recognition.
   if gestureRecognizer.view != self.yellowView && 
            gestureRecognizer.view != self.cyanView && 
            gestureRecognizer.view != self.magentaView {
      return false
   }
   // If the gesture recognizers are on diferent views, do not allow
   // simultaneous recognition.
   if gestureRecognizer.view != otherGestureRecognizer.view {
      return false
   }
   // If either gesture recognizer is a long press, do not allow
   // simultaneous recognition.
   if gestureRecognizer is UILongPressGestureRecognizer || 
          otherGestureRecognizer is UILongPressGestureRecognizer {
      return false
   }
 
   return true
}
```

## See Also

- [Preferring one gesture over another](preferring-one-gesture-over-another.md)
  Use a gesture recognizer delegate object to determine the order in which gestures are recognized in your views.
- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md)
  Learn how gesture recognizers interact with UIKit controls such as buttons switches and sliders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/allowing-the-simultaneous-recognition-of-multiple-gestures)*