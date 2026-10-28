# SPPoint3DFloatRotate

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
static SPPoint3DFloat SPPoint3DFloatRotate(SPPoint3DFloat point, SPRotation3DFloat rotation);
```

## Return Value

A point that’s rotated by the specified rotation.

## Discussion

Returns a point that’s rotated by the specified rotation around the origin.

This function is equivalent to calling @p SPPoint3DRotateAroundPoint with a zero vector for the pivot.

## Parameters

- `point`: The source point.
- `rotation`: The rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dfloatrotate)*