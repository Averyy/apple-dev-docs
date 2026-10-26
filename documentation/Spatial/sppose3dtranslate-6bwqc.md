# SPPose3DTranslate

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a transform with an origin that’s offset by the specified size structure.

**Availability**:
- iOS 16.0+ - Deprecated in 16.0
- iPadOS 16.0+ - Deprecated in 16.0
- Mac Catalyst 16.0+ - Deprecated in 16.0
- macOS 13.0+ - Deprecated in 13.0
- tvOS 16.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.0+ - Deprecated in 9.0

> **Deprecated**: Use `Vector3D` variant.

## Declaration

```c
static SPPose3D SPPose3DTranslate(SPPose3D pose, SPSize3D offset);
```

## Parameters

- `pose`: The pose to translate.
- `offset`: The size structure that defines the translation.

## See Also

### Transforming a 3D pose structure
- [SPPose3DConcatenation](./sppose3dconcatenation.md)
  Returns a pose that represents the concatenation of two poses.
- [SPPose3DFlip](./sppose3dflip.md)
  Flips a pose along the specified axis.
- [SPPose3DRotate](./sppose3drotate.md)
  Returns a transform that results from rotating with the specified rotation structure.
- [SPPose3DRotateByQuaternion](./sppose3drotatebyquaternion.md)
  Returns a transform that results from rotating with the specified quaternion.
- [SPPose3DTranslate](./sppose3dtranslate-8v4sq.md)
  Returns a pose with an origin that’s offset by the specified vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dtranslate-6bwqc)*