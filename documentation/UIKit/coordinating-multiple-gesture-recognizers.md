# Coordinating multiple gesture recognizers

**Framework**: UIKit

Discover how to use multiple gesture recognizers on the same view.

#### Overview

Gesture recognizers track incoming touch events separately, but UIKit normally allows the recognition of only one gesture at a time on a single view. Recognizing only one gesture at a time is usually preferable because it prevents user input from triggering more than one action at a time. However, this default behavior can introduce unintended side effects. For example, in a view that contains both pan and swipe gesture recognizers, swipes are never recognized. Because the pan gesture recognizer is continuous, it always recognizes its gesture before the swipe gesture recognizer, which is discrete.

To prevent the unintended side effects of the default recognition behavior, you can tell UIKit to recognize gestures in a specific order using a delegate object. UIKit uses the methods of your delegate object to determine whether a gesture recognizer must come before or after other gesture recognizers. For example, your delegate can tell UIKit that a swipe gesture recognizer must fail before a pan gesture recognizer is allowed to act. Your delegate can also tell UIKit that two gestures can be recognized simultaneously.

## Topics

### Simultaneous gestures
- [Preferring one gesture over another](preferring-one-gesture-over-another.md)
  Use a gesture recognizer delegate object to determine the order in which gestures are recognized in your views.
- [Allowing the simultaneous recognition of multiple gestures](allowing-the-simultaneous-recognition-of-multiple-gestures.md)
  Learn how to use a delegate object to allow detection of more than one gesture at a time.
- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md)
  Learn how gesture recognizers interact with UIKit controls such as buttons switches and sliders.

## See Also

- [Handling UIKit gestures](handling-uikit-gestures.md)
  Use gesture recognizers to simplify touch handling and create a consistent user experience.
- [Adopting hover support for Apple Pencil](adopting-hover-support-for-apple-pencil.md)
  Enhance user feedback for your iPadOS app with a hover preview for Apple Pencil input.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md)
  Enrich your app’s user experience by supporting standard and custom gesture interaction.
- [class UIHoverGestureRecognizer](uihovergesturerecognizer.md)
  A continuous gesture recognizer that interprets pointer movement over a view.
- [class UILongPressGestureRecognizer](uilongpressgesturerecognizer.md)
  A continuous gesture recognizer that interprets long-press gestures.
- [class UIPanGestureRecognizer](uipangesturerecognizer.md)
  A continuous gesture recognizer that interprets panning gestures.
- [class UIPinchGestureRecognizer](uipinchgesturerecognizer.md)
  A continuous gesture recognizer that interprets pinching gestures involving two touches.
- [class UIRotationGestureRecognizer](uirotationgesturerecognizer.md)
  A continuous gesture recognizer that interprets rotation gestures involving two touches.
- [class UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md)
  A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [class UISwipeGestureRecognizer](uiswipegesturerecognizer.md)
  A discrete gesture recognizer that interprets swiping gestures in one or more directions.
- [class UITapGestureRecognizer](uitapgesturerecognizer.md)
  A discrete gesture recognizer that interprets single or multiple taps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/coordinating-multiple-gesture-recognizers)*