# Transform3DProtocol Implementations

**Framework**: Spatial

## Topics

### Initializers
- [init(scale: Size3DFloat, rotation: Rotation3DFloat, translation: Vector3DFloat)](projectivetransform3dfloat/init(scale:rotation:translation:).md)
  Returns a new scale, rotate, translate transform.
- [init(shear: AxisWithFactorsFloat)](projectivetransform3dfloat/init(shear:).md)
  Returns a new shear transform
### Instance Properties
- [var inverse: ProjectiveTransform3DFloat?](projectivetransform3dfloat/inverse.md)
  The projective transform’s inverse.
- [var rotation: Rotation3DFloat?](projectivetransform3dfloat/rotation.md)
  The projective transform’s rotation.
- [var translation: Vector3DFloat](projectivetransform3dfloat/translation.md)
  The translation component
### Instance Methods
- [func flip(along: Axis3D)](projectivetransform3dfloat/flip(along:).md)
  Flips the transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3DFloat](projectivetransform3dfloat/flipped(along:).md)
  Returns the transform flipped along the specified axis.
- [func isApproximatelyEqual(to: ProjectiveTransform3DFloat, tolerance: Float) -> Bool](projectivetransform3dfloat/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](projectivetransform3dfloat/isuniform(overdimensions:).md)
  Returns `true` if the transform is affine and uniform over the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/transform3dprotocol-implementations)*