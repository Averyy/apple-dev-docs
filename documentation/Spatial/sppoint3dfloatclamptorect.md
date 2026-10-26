# SPPoint3DFloatClampToRect

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
static SPPoint3DFloat SPPoint3DFloatClampToRect(SPPoint3DFloat point, SPRect3DFloat rect);
```

#### Return Value

A point that’s clamped to the rectangle.

#### Discussion

Returns a point with coordinates clamped to the specified rectangle.

## Parameters

- `point`: The source point.
- `rect`: A 3DFloat rectangle that defines the volume to clamp the point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dfloatclamptorect)*