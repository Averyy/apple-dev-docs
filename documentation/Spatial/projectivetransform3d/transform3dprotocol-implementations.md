# Transform3DProtocol Implementations

**Framework**: Spatial

## Topics

### Initializers
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](projectivetransform3d/init(scale:rotation:translation:)-4h5wm.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(shear: AxisWithFactors)](projectivetransform3d/init(shear:).md)
  Creates a projective transform from the specified shear transform.
### Instance Properties
- [var inverse: ProjectiveTransform3D?](projectivetransform3d/inverse.md)
  The projective transform’s inverse.
- [var rotation: Rotation3D?](projectivetransform3d/rotation.md)
  The projective transform’s rotation.
- [var translation: Vector3D](projectivetransform3d/translation.md)
  The translation component of the projective transform.
### Instance Methods
- [func flip(along: Axis3D)](projectivetransform3d/flip(along:).md)
  Flips a projective transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3D](projectivetransform3d/flipped(along:).md)
  Returns a projective transform that results from flipping it along the specified axis.
- [func isApproximatelyEqual(to: ProjectiveTransform3D, tolerance: Double) -> Bool](projectivetransform3d/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](projectivetransform3d/isuniform(overdimensions:).md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/transform3dprotocol-implementations)*