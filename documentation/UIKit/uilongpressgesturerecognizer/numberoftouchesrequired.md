# numberOfTouchesRequired

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number of fingers that must touch the view for gesture recognition.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var numberOfTouchesRequired: Int { get set }
```

```objc
@property (nonatomic) NSUInteger numberOfTouchesRequired;
```

## Mentions

- [Handling long-press gestures](../handling-long-press-gestures.md)

## Discussion

The default number of fingers is `1`.

## See Also

### Configuring the gesture recognizer
- [var minimumPressDuration: TimeInterval](./minimumpressduration.md)
  The minimum time that the user must press on the view for the gesture to be recognized.
- [var numberOfTapsRequired: Int](./numberoftapsrequired.md)
  The number of taps on the view necessary for gesture recognition.
- [var allowableMovement: CGFloat](./allowablemovement.md)
  The maximum movement of the fingers on the view before the gesture fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/numberoftouchesrequired)*