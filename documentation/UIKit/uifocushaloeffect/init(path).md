# init(path:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a halo effect using the specified Bézier path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(path bezierPath: UIBezierPath)
```

```objc
+ (instancetype) effectWithPath:(UIBezierPath *) bezierPath;
```

## See Also

### Creating a halo effect
- [convenience init(roundedRect: CGRect, cornerRadius: CGFloat, curve: CALayerCornerCurve)](./init%28roundedrect,cornerradius,curve%29.md)
  Creates a rounded halo effect using the specified corner radius and corner curve.
- [convenience init(rect: CGRect)](./init%28rect%29.md)
  Creates a rectangular halo effect using the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect/init(path:))*