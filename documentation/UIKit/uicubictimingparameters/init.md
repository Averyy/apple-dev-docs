# init()

**Framework**: UIKit  
**Kind**: init

Initializes the object with the system’s default timing curve.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init()
```

#### Return Value

An initialized timing parameter object or `nil` if the object could not be created.

#### Discussion

Use this method to create a timing curve based on the default Core Animation timing function.

## See Also

- [init(animationCurve: UIView.AnimationCurve)](uicubictimingparameters/init(animationcurve:).md)
  Initializes the object with the specified UIKit timing curve.
- [init(controlPoint1: CGPoint, controlPoint2: CGPoint)](uicubictimingparameters/init(controlpoint1:controlpoint2:).md)
  Initializes the object with the specified control points for a cubic Bézier curve.
- [init?(coder: NSCoder)](uicubictimingparameters/init(coder:).md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicubictimingparameters/init())*