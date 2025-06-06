# init(animationCurve:)

**Framework**: UIKit  
**Kind**: init

Initializes the object with the specified UIKit timing curve.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(animationCurve curve: UIView.AnimationCurve)
```

#### Return Value

An initialized timing parameter object or `nil` if the object could not be created.

#### Discussion

Use this method to create a timing curve that uses the standard UIKit timing curves such as [`UIView.AnimationCurve.easeIn`](uiview/animationcurve/easein.md), [`UIView.AnimationCurve.easeOut`](uiview/animationcurve/easeout.md), [`UIView.AnimationCurve.easeInOut`](uiview/animationcurve/easeinout.md), or [`UIView.AnimationCurve.linear`](uiview/animationcurve/linear.md).

## Parameters

- `curve`: The UIKit timing curve to use for the animations. You can specify a linear animation or an animation whose initial or final speed is slightly slower.

## See Also

- [init()](uicubictimingparameters/init.md)
  Initializes the object with the system’s default timing curve.
- [init(controlPoint1: CGPoint, controlPoint2: CGPoint)](uicubictimingparameters/init(controlpoint1:controlpoint2:).md)
  Initializes the object with the specified control points for a cubic Bézier curve.
- [init?(coder: NSCoder)](uicubictimingparameters/init(coder:).md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicubictimingparameters/init(animationcurve:))*