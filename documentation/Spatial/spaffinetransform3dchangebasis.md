# SPAffineTransform3DChangeBasis

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a new affine transform structure by applying a change-of-basis.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
static SPAffineTransform3D SPAffineTransform3DChangeBasis(SPAffineTransform3D transform, SPAffineTransform3D from, SPAffineTransform3D to);
```

## See Also

### Transforming a 3D affine transform structure
- [struct Axis3D](./axis3d.md)
  Constants that describe an axis.
- [SPAffineTransform3DFlip](./spaffinetransform3dflip.md)
  Returns an affine transform that results from flipping it along the specified axis.
- [SPAffineTransform3DInvalid](./spaffinetransform3dinvalid.md)
  An affine transform that represents an invalid transform.
- [SPAffineTransform3DInverted](./spaffinetransform3dinverted.md)
  Returns a new transform that results from inverting an existing affine transform.
- [SPAffineTransform3DRotate](./spaffinetransform3drotate.md)
  Returns a transform that results from applying the specified rotation.
- [SPAffineTransform3DRotateByQuaternion](./spaffinetransform3drotatebyquaternion.md)
  Returns a transform that results from rotating with the specified quaternion.
- [SPAffineTransform3DScaleBy](./spaffinetransform3dscaleby.md)
  Returns a transform that results from scaling with the specified double-precision values.
- [SPAffineTransform3DScaleBySize](./spaffinetransform3dscalebysize.md)
  Returns a transform that results from scaling with the specified size structure.
- [SPAffineTransform3DScaleUniform](./spaffinetransform3dscaleuniform.md)
  Returns a transform that results from uniformly scaling with the specified double-precision value.
- [SPAffineTransform3DSetTranslation](./spaffinetransform3dsettranslation.md)
  Sets the translation of an affine transform.
- [SPAffineTransform3DShear](./spaffinetransform3dshear.md)
  Returns an affine transform that results from shearing over an axis by shear factors for the other two axes.
- [SPAffineTransform3DTranslate](./spaffinetransform3dtranslate-5pm5m.md)
  Returns a transform with an origin that’s offset by the specified size.
- [SPAffineTransform3DTranslate](./spaffinetransform3dtranslate-yb5g.md)
  Returns a transform with an origin that’s offset by the specified vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dchangebasis)*