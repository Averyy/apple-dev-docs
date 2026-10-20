# Transform3DProtocol Implementations

**Framework**: Spatial  
**Role**: API Collection

## Topics

### Initializers
- [init(scale: Size3DFloat, rotation: Rotation3DFloat, translation: Vector3DFloat)](./init%28scale,rotation,translation%29.md)
  Returns a new scale, rotate, translate transform.
- [init(shear: AxisWithFactorsFloat)](./init%28shear%29.md)
  Returns a new shear transform
### Instance Properties
- [var inverse: ProjectiveTransform3DFloat?](./inverse.md)
  The projective transform’s inverse.
- [var rotation: Rotation3DFloat?](./rotation.md)
  The projective transform’s rotation.
- [var translation: Vector3DFloat](./translation.md)
  The translation component
### Instance Methods
- [func flip(along: Axis3D)](./flip%28along%29.md)
  Flips the transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3DFloat](./flipped%28along%29.md)
  Returns the transform flipped along the specified axis.
- [func isApproximatelyEqual(to: ProjectiveTransform3DFloat, tolerance: Float) -> Bool](./isapproximatelyequal%28to,tolerance%29.md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](./isuniform%28overdimensions%29.md)
  Returns `true` if the transform is affine and uniform over the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/transform3dprotocol-implementations)*