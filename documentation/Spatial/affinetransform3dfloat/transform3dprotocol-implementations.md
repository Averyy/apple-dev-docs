# Transform3DProtocol Implementations

**Framework**: Spatial

## Topics

### Initializers
- [init(scale: Size3DFloat, rotation: Rotation3DFloat, translation: Vector3DFloat)](affinetransform3dfloat/init(scale:rotation:translation:).md)
  Returns a new scale, rotate, translate transform.
- [init(shear: AxisWithFactorsFloat)](affinetransform3dfloat/init(shear:).md)
  Returns a new shear transform
### Instance Properties
- [var inverse: AffineTransform3DFloat?](affinetransform3dfloat/inverse.md)
  The affine transform’s inverse.
- [var rotation: Rotation3DFloat?](affinetransform3dfloat/rotation.md)
  The affine transform’s rotation.
- [var translation: Vector3DFloat](affinetransform3dfloat/translation.md)
  The translation component
### Instance Methods
- [func flip(along: Axis3D)](affinetransform3dfloat/flip(along:).md)
  Flips the transform along the specified axis.
- [func flipped(along: Axis3D) -> AffineTransform3DFloat](affinetransform3dfloat/flipped(along:).md)
  Returns the transform flipped along the specified axis.
- [func isApproximatelyEqual(to: AffineTransform3DFloat, tolerance: Float) -> Bool](affinetransform3dfloat/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](affinetransform3dfloat/isuniform(overdimensions:).md)
  Returns `true` if the transform is uniform over the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/transform3dprotocol-implementations)*