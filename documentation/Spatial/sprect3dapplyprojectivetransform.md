# SPRect3DApplyProjectiveTransform

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

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
static SPRect3D SPRect3DApplyProjectiveTransform(SPRect3D rect, SPProjectiveTransform3D transform);
```

## Return Value

The transformed rectangle.

## Discussion

Returns a rectangle that’s transformed by the specified projective transform.

Because affine transforms do not preserve rectangles in general, this function returns the smallest rectangle that contains the transformed corner points of the `rect` parameter. If the affine transform `transform` consists solely of scaling and translation operations, then the returned rectangle coincides with the rectangle constructed from the eight transformed corners.

## Parameters

- `rect`: The source rectangle.
- `transform`: The projective transform that the function applies to the rectangle.

## See Also

### Transforming a 3D rectangle structure
- [func rotated(by: Rotation3D, around: Point3D) -> Rect3D](./rect3d/rotated%28by,around%29-3ih62.md)
  Returns a rectangle that results from applying the specified rotation around a pivot point.
- [func rotated(by: simd_quatd, around: Point3D) -> Rect3D](./rect3d/rotated%28by,around%29-8g1c9.md)
  Returns a rectangle that results from rotating with the specified quaternion around a pivot point.
- [SPRect3DApplyAffineTransform](./sprect3dapplyaffinetransform.md)
  Returns a rectangle that results from applying the specified affine transform.
- [SPRect3DApplyPose](./sprect3dapplypose.md)
  Returns a rectangle that results from applying the specified pose.
- [SPRect3DApplyScaledPose](./sprect3dapplyscaledpose.md)
  Returns a rectangle that’s transformed by the specified scaled pose.
- [SPRect3DRotate](./sprect3drotate.md)
  Returns a rectangle that results from applying the specified rotation.
- [SPRect3DRotateByQuaternion](./sprect3drotatebyquaternion.md)
  Returns a rectangle that results from rotating with the specified quaternion.
- [SPRect3DScaleBy](./sprect3dscaleby.md)
  Returns a rectangle that results from scaling with the specified double-precision values.
- [SPRect3DScaleBySize](./sprect3dscalebysize.md)
  Returns a rectangle that results from scaling with the specified size structure.
- [SPRect3DScaleUniform](./sprect3dscaleuniform.md)
  Returns a rectangle that results from uniformly scaling with the specified double-precision value.
- [SPRect3DShear](./sprect3dshear.md)
  Returns a rectangle that results from shearing over an axis by shear factors for the other two axes.
- [SPRect3DTranslate](./sprect3dtranslate-88ujj.md)
  Returns a rectangle with an origin that’s offset by the specified vector.
- [SPRect3DTranslate](./sprect3dtranslate-8amf1.md)
  Returns a rectangle with an origin that’s offset by the specified size.
- [SPRect3DUnapplyAffineTransform](./sprect3dunapplyaffinetransform.md)
  Returns a rectangle that results from unapplying the specified affine transform.
- [SPRect3DUnapplyPose](./sprect3dunapplypose.md)
  Returns a rectangle that results from unapplying the specified pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dapplyprojectivetransform)*