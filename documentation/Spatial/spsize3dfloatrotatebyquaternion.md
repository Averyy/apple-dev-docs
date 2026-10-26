# SPSize3DFloatRotateByQuaternion

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
static SPSize3DFloat SPSize3DFloatRotateByQuaternion(SPSize3DFloat size, simd_quatf quaternion);
```

#### Return Value

A size that’s rotated by the specified rotation.

#### Discussion

Returns a size that’s rotated by the specified quaternion around the origin.

## Parameters

- `size`: The source size.
- `quaternion`: The quaternion that defines the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsize3dfloatrotatebyquaternion)*