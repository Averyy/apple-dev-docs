# controlPoint2

**Framework**: UIKit  
**Kind**: property

The second control point of the cubic Bézier curve.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var controlPoint2: CGPoint { get }
```

#### Discussion

This parameter contains the point you specified at initialization time. If you initialized the object with a [`UIView.AnimationCurve`](uiview/animationcurve.md) value instead, this property is set to [`CGPointZero`](https://developer.apple.com/documentation/CoreGraphics/CGPointZero).

## See Also

- [var animationCurve: UIView.AnimationCurve](uicubictimingparameters/animationcurve.md)
  The standard UIKit animation curve to use for timing.
- [var controlPoint1: CGPoint](uicubictimingparameters/controlpoint1.md)
  The first control point for the cubic Bézier curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicubictimingparameters/controlpoint2)*