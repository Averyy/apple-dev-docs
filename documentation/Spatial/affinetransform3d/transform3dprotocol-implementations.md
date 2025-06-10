# Transform3DProtocol Implementations

**Framework**: Spatial

## Topics

### Initializers
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](affinetransform3d/init(scale:rotation:translation:)-3somu.md)
  Creates an affine transform from the specified scale, rotate, and translate transforms.
- [init(shear: AxisWithFactors)](affinetransform3d/init(shear:).md)
  Creates an affine transform from the specified shear transform.
### Instance Properties
- [var inverse: AffineTransform3D?](affinetransform3d/inverse.md)
  The affine transform’s inverse.
- [var rotation: Rotation3D?](affinetransform3d/rotation.md)
  The affine transform’s rotation.
- [var translation: Vector3D](affinetransform3d/translation.md)
  The translation component of the affine transform.
### Instance Methods
- [func flip(along: Axis3D)](affinetransform3d/flip(along:).md)
  Flips an affine transform along the specified axis.
- [func flipped(along: Axis3D) -> AffineTransform3D](affinetransform3d/flipped(along:).md)
  Returns an affine transform that results from flipping it along the specified axis.
- [func isApproximatelyEqual(to: AffineTransform3D, tolerance: Double) -> Bool](affinetransform3d/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](affinetransform3d/isuniform(overdimensions:).md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/transform3dprotocol-implementations)*