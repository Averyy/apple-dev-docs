# smoothstep(edge0:edge1:x:)

**Framework**: Spatial  
**Kind**: method

Returns a Spatial vector that represents the smooth interpolation at `x` between two vectors.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func smoothstep(edge0: Vector3DFloat, edge1: Vector3DFloat, x: Vector3DFloat) -> Vector3DFloat
```

#### Return Value

A new vector with each element set to `0` if `x <= edge0`, `1` if `x >= edge1`, and a Hermite interpolation between `0` and `1` if `edge0 < x < edge1`.

## Parameters

- `edge0`: The lower edge of the interpolation function.
- `edge1`: The upper edge of the interpolation function.
- `x`: The value that the function interpolates at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3dfloat/smoothstep(edge0:edge1:x:))*