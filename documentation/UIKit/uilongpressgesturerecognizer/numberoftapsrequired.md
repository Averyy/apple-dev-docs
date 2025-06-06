# numberOfTapsRequired

**Framework**: UIKit  
**Kind**: property

The number of taps on the view necessary for gesture recognition.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var numberOfTapsRequired: Int { get set }
```

## Mentions

- [Handling long-press gestures](handling-long-press-gestures.md)

#### Discussion

The default number of taps is `0`.

## See Also

- [var minimumPressDuration: TimeInterval](uilongpressgesturerecognizer/minimumpressduration.md)
  The minimum time that the user must press on the view for the gesture to be recognized.
- [var numberOfTouchesRequired: Int](uilongpressgesturerecognizer/numberoftouchesrequired.md)
  The number of fingers that must touch the view for gesture recognition.
- [var allowableMovement: CGFloat](uilongpressgesturerecognizer/allowablemovement.md)
  The maximum movement of the fingers on the view before the gesture fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/numberoftapsrequired)*