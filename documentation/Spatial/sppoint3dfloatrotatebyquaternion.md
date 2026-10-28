# SPPoint3DFloatRotateByQuaternion

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
static SPPoint3DFloat SPPoint3DFloatRotateByQuaternion(SPPoint3DFloat point, simd_quatf quaternion);
```

## Return Value

A point that’s rotated by the specified rotation.

## Discussion

Returns a point that’s rotated by the specified quaternion around the origin.

This function is equivalent to calling @p SPPoint3DFloatRotateByQuaternionAroundPoint with a zero vector for the pivot.

## Parameters

- `point`: The source point.
- `quaternion`: The quaternion that defines the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dfloatrotatebyquaternion)*