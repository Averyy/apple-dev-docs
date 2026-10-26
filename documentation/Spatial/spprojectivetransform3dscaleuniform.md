# SPProjectiveTransform3DScaleUniform

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a transform that results from uniformly scaling with the specified double-precision value.

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
static SPProjectiveTransform3D SPProjectiveTransform3DScaleUniform(SPProjectiveTransform3D transform, double scale);
```

#### Return Value

The transform that results from uniformly scaling with the specified double-precision value.

## Parameters

- `transform`: The projective transform to scale uniformly.
- `scale`: The double-precision value that species the uniform scale.

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
- [SPProjectiveTransform3DRotate](./spprojectivetransform3drotate.md)
  Returns a transform that results from applying the specified rotation.
- [SPProjectiveTransform3DRotateByQuaternion](./spprojectivetransform3drotatebyquaternion.md)
  Returns a transform that results from rotating with the specified quaternion.
- [SPProjectiveTransform3DScaleBySize](./spprojectivetransform3dscalebysize.md)
  Returns a transform that results from scaling with the specified size structure.
- [SPProjectiveTransform3DTranslate](./spprojectivetransform3dtranslate-4tynj.md)
  Returns a transform with an origin that’s offset by the specified size.
- [SPProjectiveTransform3DTranslate](./spprojectivetransform3dtranslate-7ecid.md)
  Returns a transform with an origin that’s offset by the specified vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dscaleuniform)*