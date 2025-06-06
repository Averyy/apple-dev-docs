# init(controlPoint1:controlPoint2:)

**Framework**: UIKit  
**Kind**: init

Initializes the object with the specified control points for a cubic Bézier curve.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(controlPoint1 point1: CGPoint, controlPoint2 point2: CGPoint)
```

#### Return Value

An initialized timing parameter object or `nil` if the object could not be created.

#### Discussion

Use this method to initialize the timing curve with a custom cubic Bézier curve. The curve consists of a line whose starting point is (0, 0), whose end point is (1, 1), and whose shape is defined by `point1` and `point2`.

## Parameters

- `point1`: The first control point for the cubic Bézier timing curve. The x and y values of this point must be in the range   to  .
- `point2`: The second control point for the cubic Bézier timing curve. The x and y values of this point must be in the range   to  .

## See Also

- [init()](uicubictimingparameters/init.md)
  Initializes the object with the system’s default timing curve.
- [init(animationCurve: UIView.AnimationCurve)](uicubictimingparameters/init(animationcurve:).md)
  Initializes the object with the specified UIKit timing curve.
- [init?(coder: NSCoder)](uicubictimingparameters/init(coder:).md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicubictimingparameters/init(controlpoint1:controlpoint2:))*