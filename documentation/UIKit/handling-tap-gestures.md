# Handling tap gestures

**Framework**: UIKit

Use brief taps on the screen to implement button-like interactions with your content.

#### Overview

Tap gestures detect one or more fingers touching the screen briefly. The fingers involved in these gestures must not move significantly from the initial touch points, and you can configure the number of times the fingers must touch the screen. For example, you might configure tap gesture recognizers to detect single taps, double taps, or triple taps.

You can attach a gesture recognizer in one of these ways:

- Programmatically. Call the [`addGestureRecognizer(_:)`](uiview/addgesturerecognizer(_:).md) method of your view.
- In Interface Builder. Drag the appropriate object from the library and drop it onto your view.

![A diagram showing a single-finger tap gesture](https://docs-assets.developer.apple.com/published/036f7d602568a88e8e03f3a5ef12b610/media-3004402%402x.png)

A [`UITapGestureRecognizer`](uitapgesturerecognizer.md) object provides event handling capabilities similar to those of a button — it detects a tap in its view and reports that tap to your action method. Tap gestures are discrete, so your action method is called only when the tap gesture is recognized successfully. You can configure a tap gesture recognizer to require any number of taps — for example, single taps or double taps — before your action method is called.

The following code shows an action method that responds to a successful tap in a view by animating that view to a new location. Always check the gesture recognizer’s [`state`](uigesturerecognizer/state-swift.property.md) property before taking any actions, even for a discrete gesture recognizer.

```swift
@IBAction func tapPiece(_ gestureRecognizer : UITapGestureRecognizer ) {
   guard gestureRecognizer.view != nil else { return }
        
   if gestureRecognizer.state == .ended {      // Move the view down and to the right when tapped.
      let animator = UIViewPropertyAnimator(duration: 0.2, curve: .easeInOut, animations: {
         gestureRecognizer.view!.center.x += 100
         gestureRecognizer.view!.center.y += 100
      })
      animator.startAnimation()
   }}

```

If the code for your tap gesture recognizer isn’t called, check to see if the following conditions are true, and make corrections as needed:

- The [`isUserInteractionEnabled`](uiview/isuserinteractionenabled.md) property of the view is set to [`true`](https://developer.apple.com/documentation/swift/true). Image views and labels set this property to [`false`](https://developer.apple.com/documentation/swift/false) by default.
- The number of taps was equal to the number specified in the [`numberOfTapsRequired`](uitapgesturerecognizer/numberoftapsrequired.md) property.
- The number of fingers was equal to the number specified in the [`numberOfTouchesRequired`](uitapgesturerecognizer/numberoftouchesrequired.md) property.

## See Also

- [Handling long-press gestures](handling-long-press-gestures.md)
  Detect extended duration taps on the screen, and use them to reveal contextually relevant content.
- [Handling pan gestures](handling-pan-gestures.md)
  Trace the movement of fingers around the screen, and apply that movement to your content.
- [Handling swipe gestures](handling-swipe-gestures.md)
  Detect a horizontal or vertical swipe motion on the screen, and use it to trigger navigation through your content.
- [Handling pinch gestures](handling-pinch-gestures.md)
  Track the distance between two fingers and use that information to scale or zoom your content.
- [Handling rotation gestures](handling-rotation-gestures.md)
  Measure the relative rotation of two fingers on the screen, and use that motion to rotate your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/handling-tap-gestures)*