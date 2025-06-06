# minimumPressDuration

**Framework**: UIKit  
**Kind**: property

The minimum time that the user must press on the view for the gesture to be recognized.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minimumPressDuration: TimeInterval { get set }
```

## Mentions

- [Handling long-press gestures](handling-long-press-gestures.md)

#### Discussion

The time interval is in seconds. The default duration is `0.5` seconds.

## See Also

- [var numberOfTouchesRequired: Int](uilongpressgesturerecognizer/numberoftouchesrequired.md)
  The number of fingers that must touch the view for gesture recognition.
- [var numberOfTapsRequired: Int](uilongpressgesturerecognizer/numberoftapsrequired.md)
  The number of taps on the view necessary for gesture recognition.
- [var allowableMovement: CGFloat](uilongpressgesturerecognizer/allowablemovement.md)
  The maximum movement of the fingers on the view before the gesture fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/minimumpressduration)*