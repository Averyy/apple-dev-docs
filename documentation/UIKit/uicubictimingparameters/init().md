# init()

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes the object with the system’s default timing curve.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Return Value

An initialized timing parameter object or `nil` if the object could not be created.

#### Discussion

Use this method to create a timing curve based on the default Core Animation timing function.

## See Also

### Initializing a cubic timing parameters object
- [init(animationCurve: UIView.AnimationCurve)](./init%28animationcurve%29.md)
  Initializes the object with the specified UIKit timing curve.
- [init(controlPoint1: CGPoint, controlPoint2: CGPoint)](./init%28controlpoint1,controlpoint2%29.md)
  Initializes the object with the specified control points for a cubic Bézier curve.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicubictimingparameters/init())*