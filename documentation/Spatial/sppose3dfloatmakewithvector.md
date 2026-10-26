# SPPose3DFloatMakeWithVector

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
static SPPose3DFloat SPPose3DFloatMakeWithVector(simd_float3 position, simd_quatf rotation);
```

#### Return Value

A new pose structure.

#### Discussion

Returns a pose with the specified position and rotation.

## Parameters

- `position`: A point structure that specifies the position of the pose.
- `rotation`: A rotation structure that specifies the rotation of the pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatmakewithvector)*