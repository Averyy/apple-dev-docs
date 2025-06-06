# animationCurve

**Framework**: UIKit  
**Kind**: property

The standard UIKit animation curve to use for timing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var animationCurve: UIView.AnimationCurve { get }
```

#### Discussion

If you initialized this object using an animation curve, this property reflects the curve you specified. If you initialized the object using the control points for a cubic Bézier curve, the value of this property is undefined.

## See Also

- [var controlPoint1: CGPoint](uicubictimingparameters/controlpoint1.md)
  The first control point for the cubic Bézier curve.
- [var controlPoint2: CGPoint](uicubictimingparameters/controlpoint2.md)
  The second control point of the cubic Bézier curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicubictimingparameters/animationcurve)*