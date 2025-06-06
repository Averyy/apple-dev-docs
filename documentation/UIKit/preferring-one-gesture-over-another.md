# Preferring one gesture over another

**Framework**: UIKit

Use a gesture recognizer delegate object to determine the order in which gestures are recognized in your views.

#### Overview

For any two gesture recognizers involved in a potential conflict, only one needs an associated delegate object, and that object must conform to the [`UIGestureRecognizerDelegate`](uigesturerecognizerdelegate.md) protocol. In your delegate, implement the methods you need for the appropriate resolution. The best way to see how to use these methods is with a few examples.

The following code shows how to recognize tap and double-tap gestures in the same view. The view in this example has two [`UITapGestureRecognizer`](uitapgesturerecognizer.md) objects, one of which is configured to require two taps. Normally, the single-tap gesture would always be recognized before the double-tap gesture, but you can use the [`gestureRecognizer(_:shouldRequireFailureOf:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md) method to reverse that behavior. The implementation of this method prevents the single-tap gesture from being recognized until after the double-tap gesture recognizer explicitly reaches the failed state, which happens when the touch sequence contains only one tap.

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
         shouldRequireFailureOf otherGestureRecognizer: UIGestureRecognizer) -> Bool {
   // Don't recognize a single tap until a double-tap fails.
   if gestureRecognizer == self.tapGesture && 
          otherGestureRecognizer == self.doubleTapGesture {
      return true
   }
   return false
}
```

The following code shows how to recognize a swipe gesture before a pan gesture. In this case, the delegate object is attached to the swipe gesture recognizer and implements the [`gestureRecognizer(_:shouldBeRequiredToFailBy:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:).md) method. The logic of this method prevents the pan gesture from being recognized until the swipe gesture fails.

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
         shouldBeRequiredToFailBy otherGestureRecognizer: UIGestureRecognizer) -> Bool {
   // Do not begin the pan until the swipe fails. 
   if gestureRecognizer == self.swipeGesture && 
          otherGestureRecognizer == self.panGesture {
      return true
   }
   return false
}
```

The following code shows an alternative way to configure the dependency between a swipe and a pan gesture. Instead of attaching a delegate object to the swipe gesture, this example attaches the delegate to the pan gesture. Because of the change, the delegate must now implement the [`gestureRecognizer(_:shouldRequireFailureOf:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md) method and require the swipe to fail. The end results are the same as those from the previous example.

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
         shouldRequireFailureOf otherGestureRecognizer: UIGestureRecognizer) -> Bool {
   if gestureRecognizer == self.panGesture && 
          otherGestureRecognizer == self.swipeGesture {
      return true
   }
   return false
}
```

The ability to attach a delegate to any gesture recognizer lets you create complex dependency chains among your gestures. For more information about regulating gesture recognition, see [`UIGestureRecognizerDelegate`](uigesturerecognizerdelegate.md).

## See Also

- [Allowing the simultaneous recognition of multiple gestures](allowing-the-simultaneous-recognition-of-multiple-gestures.md)
  Learn how to use a delegate object to allow detection of more than one gesture at a time.
- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md)
  Learn how gesture recognizers interact with UIKit controls such as buttons switches and sliders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/preferring-one-gesture-over-another)*