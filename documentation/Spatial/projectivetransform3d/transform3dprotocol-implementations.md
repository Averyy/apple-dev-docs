# Transform3DProtocol Implementations

**Framework**: Spatial  
**Role**: API Collection

## Topics

### Initializers
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](./init%28scale,rotation,translation%29-4h5wm.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(shear: AxisWithFactors)](./init%28shear%29.md)
  Creates a projective transform from the specified shear transform.
### Instance Properties
- [var inverse: ProjectiveTransform3D?](./inverse.md)
  The projective transform’s inverse.
- [var rotation: Rotation3D?](./rotation.md)
  The projective transform’s rotation.
- [var translation: Vector3D](./translation.md)
  The translation component of the projective transform.
### Instance Methods
- [func flip(along: Axis3D)](./flip%28along%29.md)
  Flips a projective transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3D](./flipped%28along%29.md)
  Returns a projective transform that results from flipping it along the specified axis.
- [func isApproximatelyEqual(to: ProjectiveTransform3D, tolerance: Double) -> Bool](./isapproximatelyequal%28to,tolerance%29.md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](./isuniform%28overdimensions%29.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/transform3dprotocol-implementations)*