# SPPoint3DClampToRect

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPPoint3D SPPoint3DClampToRect(SPPoint3D point, SPRect3D rect);
```

## Return Value

A point that’s clamped to the rectangle.

## Discussion

Returns a point with coordinates clamped to the specified rectangle.

## Parameters

- `point`: The source point.
- `rect`: A 3D rectangle that defines the volume to clamp the point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dclamptorect)*