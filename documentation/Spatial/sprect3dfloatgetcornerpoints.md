# SPRect3DFloatGetCornerPoints

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
static void SPRect3DFloatGetCornerPoints(SPRect3DFloat rect, SPPoint3DFloat points[]);
```

## Discussion

Returns the corner points of the specified rectangle.

This function returns the vertices in a clockwise direction, starting from the origin:

```
    5-----6
    |     |
    1-----2  |
    |  |  |  |         y  z
    |  4--|--7         | /
    |     |            |/
    0-----3            +-- x
```

For example, @p points[0] equals @p rect.origin, and @p points[6] is at @p rect.origin offset by @p rect.size.

## Parameters

- `rect`: The 3DFloat rectangle that provides the points.
- `points`: An array of eight points that the function populates with the corner points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatgetcornerpoints)*