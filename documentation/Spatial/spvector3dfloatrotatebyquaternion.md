# SPVector3DFloatRotateByQuaternion

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
static SPVector3DFloat SPVector3DFloatRotateByQuaternion(SPVector3DFloat vector, simd_quatf quaternion);
```

## Return Value

A vector that’s rotated by the specified quaternion.

## Discussion

Returns a vector that’s rotated by the specified quaternion around the origin.

## Parameters

- `vector`: The source vector.
- `quaternion`: The quaternion that defines the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3dfloatrotatebyquaternion)*