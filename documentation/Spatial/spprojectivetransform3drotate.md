# SPProjectiveTransform3DRotate

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a transform that results from applying the specified rotation.

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
static SPProjectiveTransform3D SPProjectiveTransform3DRotate(SPProjectiveTransform3D transform, SPRotation3D rotation);
```

## Return Value

The transform that results from applying the specified rotation.

## Parameters

- `transform`: The affine transform to rotate.
- `rotation`: The rotation structure that defines the rotation’s angle and axis.

## See Also

### Transforming a 3D projective transform structure
- [SPProjectiveTransform3DScaleBy](./spprojectivetransform3dscaleby.md)
  Returns a transform that results from scaling with the specified double-precision values.
- [SPProjectiveTransform3DShear](./spprojectivetransform3dshear.md)
  Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.
- [struct Axis3D](./axis3d.md)
  Constants that describe an axis.
- [SPProjectiveTransform3DFlip](./spprojectivetransform3dflip.md)
  Returns a projective transform that results from flipping it along the specified axis.
- [SPProjectiveTransform3DInverted](./spprojectivetransform3dinverted.md)
  Returns a new transform that results from inverting an existing projective transform.
- [SPProjectiveTransform3DSetTranslation](./spprojectivetransform3dsettranslation.md)
  Sets the translation of a projective transform.
- [SPProjectiveTransform3DRotateByQuaternion](./spprojectivetransform3drotatebyquaternion.md)
  Returns a transform that results from rotating with the specified quaternion.
- [SPProjectiveTransform3DScaleBySize](./spprojectivetransform3dscalebysize.md)
  Returns a transform that results from scaling with the specified size structure.
- [SPProjectiveTransform3DScaleUniform](./spprojectivetransform3dscaleuniform.md)
  Returns a transform that results from uniformly scaling with the specified double-precision value.
- [SPProjectiveTransform3DTranslate](./spprojectivetransform3dtranslate-4tynj.md)
  Returns a transform with an origin that’s offset by the specified size.
- [SPProjectiveTransform3DTranslate](./spprojectivetransform3dtranslate-7ecid.md)
  Returns a transform with an origin that’s offset by the specified vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3drotate)*