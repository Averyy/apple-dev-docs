# SPAffineTransform3DRotateByQuaternion

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a transform that results from rotating with the specified quaternion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPAffineTransform3D SPAffineTransform3DRotateByQuaternion(SPAffineTransform3D transform, simd_quatd quaternion);
```

## Return Value

The transform that results from rotating with the specified quaternion.

## Parameters

- `transform`: The transform object to rotate.
- `quaternion`: The double-precision quaternion that specifies the rotation.

## See Also

### Transforming a 3D affine transform structure
- [struct Axis3D](./axis3d.md)
  Constants that describe an axis.
- [SPAffineTransform3DChangeBasis](./spaffinetransform3dchangebasis.md)
  Returns a new affine transform structure by applying a change-of-basis.
- [SPAffineTransform3DFlip](./spaffinetransform3dflip.md)
  Returns an affine transform that results from flipping it along the specified axis.
- [SPAffineTransform3DInvalid](./spaffinetransform3dinvalid.md)
  An affine transform that represents an invalid transform.
- [SPAffineTransform3DInverted](./spaffinetransform3dinverted.md)
  Returns a new transform that results from inverting an existing affine transform.
- [SPAffineTransform3DRotate](./spaffinetransform3drotate.md)
  Returns a transform that results from applying the specified rotation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3drotatebyquaternion)*