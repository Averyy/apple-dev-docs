# SPPose3DFloatRotateByQuaternion

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
static SPPose3DFloat SPPose3DFloatRotateByQuaternion(SPPose3DFloat pose, simd_quatf quaternion);
```

#### Return Value

A pose with a rotation that’s rotated by the specified quaternion.

#### Discussion

Returns a pose with a rotation that’s rotated by the specified quaternion.

## Parameters

- `pose`: The source pose.
- `quaternion`: The quaternion that defines the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatrotatebyquaternion)*