# scale

**Framework**: UIKit  
**Kind**: property

The scale factor relative to the points of the two touches in screen coordinates.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var scale: CGFloat { get set }
```

## Mentions

- [Handling pinch gestures](handling-pinch-gestures.md)

#### Discussion

You may set the scale factor, but doing so resets the velocity.

The scale value is an absolute value that varies over time. It isn’t the delta value from the last time that the scale was reported. Apply the scale value to the state of the view when the gesture is first recognized — don’t concatenate the value each time the handler is called.

## See Also

- [var velocity: CGFloat](uipinchgesturerecognizer/velocity.md)
  The velocity of the pinch in scale factor per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipinchgesturerecognizer/scale)*