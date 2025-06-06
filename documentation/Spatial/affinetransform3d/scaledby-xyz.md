# scaledBy(x:y:z:)

**Framework**: Spatial  
**Kind**: method

Returns a transform that results from scaling with specified double-precision values.

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
func scaledBy(x: Double = 1, y: Double = 1, z: Double = 1) -> AffineTransform3D
```

#### Return Value

The transform that results from scaling with specified double-precision values.

## Parameters

- `x`: The double-precision value that specifies the scale along the width dimension.
- `y`: The double-precision value that specifies the scale along the height dimension.
- `z`: The double-precision value that specifies the scale along the depth dimension.

## See Also

- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
- [enum AxisWithFactors](axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [func changeBasis(from: AffineTransform3D, to: AffineTransform3D) -> AffineTransform3D?](affinetransform3d/changebasis(from:to:).md)
  Returns a new affine transform structure by applying a change-of-basis.
- [func concatenating(AffineTransform3D) -> AffineTransform3D](affinetransform3d/concatenating(_:).md)
  Returns an affine transformation matrix that results from concatenating two existing affine transforms.
- [func flip(along: Axis3D)](affinetransform3d/flip(along:).md)
  Flips an affine transform along the specified axis.
- [func flipped(along: Axis3D) -> AffineTransform3D](affinetransform3d/flipped(along:).md)
  Returns an affine transform that results from flipping it along the specified axis.
- [var inverse: AffineTransform3D?](affinetransform3d/inverse.md)
  The affine transform’s inverse.
- [func sheared(AxisWithFactors) -> AffineTransform3D](affinetransform3d/sheared(_:).md)
  Returns an affine transform that results from shearing over an axis by shear factors for the other two axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/scaledby(x:y:z:))*