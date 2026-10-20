# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a timing parameters object from data in an unarchiver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Initializing a cubic timing parameters object
- [init()](./init%28%29.md)
  Initializes the object with the system’s default timing curve.
- [init(animationCurve: UIView.AnimationCurve)](./init%28animationcurve%29.md)
  Initializes the object with the specified UIKit timing curve.
- [init(controlPoint1: CGPoint, controlPoint2: CGPoint)](./init%28controlpoint1,controlpoint2%29.md)
  Initializes the object with the specified control points for a cubic Bézier curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicubictimingparameters/init(coder:))*