# CATransform3D

**Framework**: Core Animation  
**Kind**: struct

The standard transform matrix used throughout Core Animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CATransform3D
```

#### Overview

The transform matrix is used to rotate, scale, translate, skew, and project the layer content. Functions are provided for creating, concatenating, and modifying CATransform3D data.

## Topics

### Initializers
- [init()](catransform3d/init.md)
- [init(m11: CGFloat, m12: CGFloat, m13: CGFloat, m14: CGFloat, m21: CGFloat, m22: CGFloat, m23: CGFloat, m24: CGFloat, m31: CGFloat, m32: CGFloat, m33: CGFloat, m34: CGFloat, m41: CGFloat, m42: CGFloat, m43: CGFloat, m44: CGFloat)](catransform3d/init(m11:m12:m13:m14:m21:m22:m23:m24:m31:m32:m33:m34:m41:m42:m43:m44:).md)
- [init(float4x4)](catransform3d/init(_:)-6awvy.md)
- [init(double4x4)](catransform3d/init(_:)-6euzs.md)
### Instance Properties
- [var m11: CGFloat](catransform3d/m11.md)
  The entry at position 1,1 in the matrix.
- [var m12: CGFloat](catransform3d/m12.md)
  The entry at position 1,2 in the matrix.
- [var m13: CGFloat](catransform3d/m13.md)
  The entry at position 1,3 in the matrix.
- [var m14: CGFloat](catransform3d/m14.md)
  The entry at position 1,4 in the matrix.
- [var m21: CGFloat](catransform3d/m21.md)
  The entry at position 2,1 in the matrix.
- [var m22: CGFloat](catransform3d/m22.md)
  The entry at position 2,2 in the matrix.
- [var m23: CGFloat](catransform3d/m23.md)
  The entry at position 2,3 in the matrix.
- [var m24: CGFloat](catransform3d/m24.md)
  The entry at position 2,4 in the matrix.
- [var m31: CGFloat](catransform3d/m31.md)
  The entry at position 3,1 in the matrix.
- [var m32: CGFloat](catransform3d/m32.md)
  The entry at position 3,2 in the matrix.
- [var m33: CGFloat](catransform3d/m33.md)
  The entry at position 3,3 in the matrix.
- [var m34: CGFloat](catransform3d/m34.md)
  The entry at position 3,4 in the matrix.
- [var m41: CGFloat](catransform3d/m41.md)
  The entry at position 4,1 in the matrix.
- [var m42: CGFloat](catransform3d/m42.md)
  The entry at position 4,2 in the matrix.
- [var m43: CGFloat](catransform3d/m43.md)
  The entry at position 4,3 in the matrix.
- [var m44: CGFloat](catransform3d/m44.md)
  The entry at position 4,4 in the matrix.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CAAutoresizingMask](caautoresizingmask.md)
  These constants are used by the [`autoresizingMask`](calayer/autoresizingmask.md) property.
- [Action Identifiers](action-identifiers.md)
  These constants are the predefined action identifiers used by [`action(forKey:)`](calayer/action(forkey:).md), [`add(_:forKey:)`](calayer/add(_:forkey:).md), [`defaultAction(forKey:)`](calayer/defaultaction(forkey:).md), [`removeAnimation(forKey:)`](calayer/removeanimation(forkey:).md), Layer Filters, and the [`CAAction`](caaction.md) protocol method [`run(forKey:object:arguments:)`](caaction/run(forkey:object:arguments:).md).
- [struct CAEdgeAntialiasingMask](caedgeantialiasingmask.md)
  This mask is used by the [`edgeAntialiasingMask`](calayer/edgeantialiasingmask.md) property.
- [Identity Transform](identity-transform.md)
  Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md)
  These constants specify the scaling filters used by [`magnificationFilter`](calayer/magnificationfilter.md) and [`minificationFilter`](calayer/minificationfilter.md).
- [CALayer.DynamicRange](calayer/dynamicrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3d)*