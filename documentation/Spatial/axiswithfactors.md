# AxisWithFactors

**Framework**: Spatial  
**Kind**: enum

Constants that describe the axis of a shear transform.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum AxisWithFactors
```

## Topics

### Enumeration cases
- [case xAxis(yShearFactor: Double, zShearFactor: Double)](axiswithfactors/xaxis(yshearfactor:zshearfactor:).md)
  Shears over the x-axis with shear factors for the y- and z-axis.
- [case yAxis(xShearFactor: Double, zShearFactor: Double)](axiswithfactors/yaxis(xshearfactor:zshearfactor:).md)
  Shears over the y-axis with shear factors for the x- and z-axis.
- [case zAxis(xShearFactor: Double, yShearFactor: Double)](axiswithfactors/zaxis(xshearfactor:yshearfactor:).md)
  Shears over the z-axis with shear factors for the x- and y-axis.

## See Also

- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
- [func changeBasis(from: AffineTransform3D, to: AffineTransform3D) -> AffineTransform3D?](affinetransform3d/changebasis(from:to:).md)
  Returns a new affine transform structure by applying a change-of-basis.
- [func flip(along: Axis3D)](affinetransform3d/flip(along:).md)
  Flips an affine transform along the specified axis.
- [func flipped(along: Axis3D) -> AffineTransform3D](affinetransform3d/flipped(along:).md)
  Returns an affine transform that results from flipping it along the specified axis.
- [var inverse: AffineTransform3D?](affinetransform3d/inverse.md)
  The affine transform’s inverse.
- [func scaledBy(x: Double, y: Double, z: Double) -> AffineTransform3D](affinetransform3d/scaledby(x:y:z:).md)
  Returns a transform that results from scaling with specified double-precision values.
- [func sheared(AxisWithFactors) -> AffineTransform3D](affinetransform3d/sheared(_:).md)
  Returns an affine transform that results from shearing over an axis by shear factors for the other two axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/axiswithfactors)*