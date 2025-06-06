# UIPanGestureRecognizer

**Framework**: UIKit  
**Kind**: class

A continuous gesture recognizer that interprets panning gestures.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPanGestureRecognizer
```

## Mentions

- [Handling pan gestures](handling-pan-gestures.md)

#### Overview

[`UIPanGestureRecognizer`](uipangesturerecognizer.md) is a concrete subclass of [`UIGestureRecognizer`](uigesturerecognizer.md).

Clients of this class can, in their action methods, query the [`UIPanGestureRecognizer`](uipangesturerecognizer.md) object for the current translation of the gesture ([`translation(in:)`](uipangesturerecognizer/translation(in:).md)) and the velocity of the translation ([`velocity(in:)`](uipangesturerecognizer/velocity(in:).md)). They can specify a view’s coordinate system to use for the translation and velocity values. Clients can also reset the translation to a desired value.

A panning gesture is continuous. The user must press one or more fingers on a view while panning it. The gesture begins ([`UIGestureRecognizer.State.began`](uigesturerecognizer/state-swift.enum/began.md)) when the user moves the minimum number of fingers allowed ([`minimumNumberOfTouches`](uipangesturerecognizer/minimumnumberoftouches.md)) enough distance for recognition as a pan. It changes ([`UIGestureRecognizer.State.changed`](uigesturerecognizer/state-swift.enum/changed.md)) when the user moves a finger while pressing with the minimum number of fingers. It ends ([`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md)) when the user lifts all fingers.

## Topics

### Configuring the gesture recognizer
- [var maximumNumberOfTouches: Int](uipangesturerecognizer/maximumnumberoftouches.md)
  The maximum number of fingers that can touch the view for gesture recognition.
- [var minimumNumberOfTouches: Int](uipangesturerecognizer/minimumnumberoftouches.md)
  The minimum number of fingers that can touch the view for gesture recognition.
### Tracking the location and velocity of the gesture
- [func translation(in: UIView?) -> CGPoint](uipangesturerecognizer/translation(in:).md)
  Interprets the pan gesture in the coordinate system of the specified view.
- [func setTranslation(CGPoint, in: UIView?)](uipangesturerecognizer/settranslation(_:in:).md)
  Sets the translation value in the coordinate system of the specified view.
- [func velocity(in: UIView?) -> CGPoint](uipangesturerecognizer/velocity(in:).md)
  Interprets the velocity of the pan gesture in the coordinate system of the specified view.
### Tracking scroll events
- [var allowedScrollTypesMask: UIScrollTypeMask](uipangesturerecognizer/allowedscrolltypesmask.md)
  A scroll type mask that enables recognition of scroll events.
- [struct UIScrollTypeMask](uiscrolltypemask.md)
  A bit mask identifying the scroll type of a pan gesture.
- [enum UIScrollType](uiscrolltype.md)
  Constants that define the type of the scroll.

## Relationships

### Inherits From
- [UIGestureRecognizer](uigesturerecognizer.md)
### Inherited By
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Handling UIKit gestures](handling-uikit-gestures.md)
  Use gesture recognizers to simplify touch handling and create a consistent user experience.
- [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md)
  Discover how to use multiple gesture recognizers on the same view.
- [Adopting hover support for Apple Pencil](adopting-hover-support-for-apple-pencil.md)
  Enhance user feedback for your iPadOS app with a hover preview for Apple Pencil input.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md)
  Enrich your app’s user experience by supporting standard and custom gesture interaction.
- [class UIHoverGestureRecognizer](uihovergesturerecognizer.md)
  A continuous gesture recognizer that interprets pointer movement over a view.
- [class UILongPressGestureRecognizer](uilongpressgesturerecognizer.md)
  A continuous gesture recognizer that interprets long-press gestures.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer)*