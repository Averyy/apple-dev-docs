# SPRect3DFloatRotate

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
static SPRect3DFloat SPRect3DFloatRotate(SPRect3DFloat rect, SPRotation3DFloat rotation);
```

## Return Value

A rectangle that’s rotated by the specified rotation.

## Discussion

Returns a rectangle that’s rotated by the specified rotation around the origin.

This function is equivalent to calling @p SPRect3DFloatRotateAroundPoint with a zero vector for the pivot.

Because affine transforms do not preserve rectangles in general, this function returns the smallest rectangle that contains the transformed corner points of the `rect` parameter.

## Parameters

- `rect`: The source rectangle.
- `rotation`: The rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatrotate)*