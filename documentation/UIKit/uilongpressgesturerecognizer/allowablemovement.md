# allowableMovement

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum movement of the fingers on the view before the gesture fails.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var allowableMovement: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat allowableMovement;
```

#### Discussion

The allowable distance, measured in points. The default distance is `10` points.

## See Also

### Configuring the gesture recognizer
- [var minimumPressDuration: TimeInterval](./minimumpressduration.md)
  The minimum time that the user must press on the view for the gesture to be recognized.
- [var numberOfTouchesRequired: Int](./numberoftouchesrequired.md)
  The number of fingers that must touch the view for gesture recognition.
- [var numberOfTapsRequired: Int](./numberoftapsrequired.md)
  The number of taps on the view necessary for gesture recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/allowablemovement)*