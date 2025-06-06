# allowableMovement

**Framework**: UIKit  
**Kind**: property

The maximum movement of the fingers on the view before the gesture fails.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowableMovement: CGFloat { get set }
```

#### Discussion

The allowable distance, measured in points. The default distance is `10` points.

## See Also

- [var minimumPressDuration: TimeInterval](uilongpressgesturerecognizer/minimumpressduration.md)
  The minimum time that the user must press on the view for the gesture to be recognized.
- [var numberOfTouchesRequired: Int](uilongpressgesturerecognizer/numberoftouchesrequired.md)
  The number of fingers that must touch the view for gesture recognition.
- [var numberOfTapsRequired: Int](uilongpressgesturerecognizer/numberoftapsrequired.md)
  The number of taps on the view necessary for gesture recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/allowablemovement)*