# SPScaledPose3DFloatRotateByQuaternion

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPScaledPose3DFloat SPScaledPose3DFloatRotateByQuaternion(SPScaledPose3DFloat scaledPose, simd_quatf quaternion);
```

#### Return Value

A scaled pose with a rotation that’s rotated by the specified quaternion.

#### Discussion

Returns a scaled pose with a rotation that’s rotated by the specified quaternion.

## Parameters

- `scaledPose`: The source scaled pose.
- `quaternion`: The quaternion that defines the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatrotatebyquaternion)*