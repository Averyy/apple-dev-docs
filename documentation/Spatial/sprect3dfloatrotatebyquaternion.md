# SPRect3DFloatRotateByQuaternion

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
static SPRect3DFloat SPRect3DFloatRotateByQuaternion(SPRect3DFloat rect, simd_quatf quaternion);
```

#### Return Value

A rectangle that’s rotated by the specified rotation.

#### Discussion

Returns a rectangle that’s rotated by the specified quaternion around the origin.

This function is equivalent to calling @p SPRect3DFloatRotateByQuaternionAroundPoint with a zero vector for the pivot.

Because affine transforms do not preserve rectangles in general, this function returns the smallest rectangle that contains the transformed corner points of the `rect` parameter.

## Parameters

- `rect`: The source rectangle.
- `quaternion`: The quaternion that defines the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatrotatebyquaternion)*