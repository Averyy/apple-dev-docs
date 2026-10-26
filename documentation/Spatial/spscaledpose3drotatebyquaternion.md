# SPScaledPose3DRotateByQuaternion

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a scaled pose with a rotation that’s rotated by the specified quaternion.

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
static SPScaledPose3D SPScaledPose3DRotateByQuaternion(SPScaledPose3D scaledPose, simd_quatd quaternion);
```

## See Also

### Transforming a 3D scaled-pose structure
- [SPScaledPose3DFlip](./spscaledpose3dflip.md)
  Returns a scaled pose that’s flipped along the specified axis.
- [SPScaledPose3DRotate](./spscaledpose3drotate.md)
  Returns a scaled pose with a rotation that’s rotated by the specified rotation.
- [SPScaledPose3DTranslate](./spscaledpose3dtranslate.md)
  Returns a scaled pose with an origin that’s offset by the specified vector.
- [SPScaledPose3DConcatenation](./spscaledpose3dconcatenation-7ljg6.md)
  Returns a new scaled pose that’s constructed by concatenating two existing poses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3drotatebyquaternion)*