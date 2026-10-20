# init(roundedRect:cornerRadius:curve:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a rounded halo effect using the specified corner radius and corner curve.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(roundedRect rect: CGRect, cornerRadius: CGFloat, curve: CALayerCornerCurve)
```

```objc
+ (instancetype) effectWithRoundedRect:(CGRect) rect cornerRadius:(CGFloat) cornerRadius curve:(CALayerCornerCurve) curve;
```

## See Also

### Creating a halo effect
- [convenience init(rect: CGRect)](./init%28rect%29.md)
  Creates a rectangular halo effect using the specified rectangle.
- [convenience init(path: UIBezierPath)](./init%28path%29.md)
  Creates a halo effect using the specified Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect/init(roundedrect:cornerradius:curve:))*