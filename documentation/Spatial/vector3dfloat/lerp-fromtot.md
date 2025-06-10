# lerp(from:to:t:)

**Framework**: Spatial  
**Kind**: method

Returns a Spatial vector that represents the linear interpolation at `t` between two vectors.

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
static func lerp(from: Vector3DFloat, to: Vector3DFloat, t: Vector3DFloat) -> Vector3DFloat
```

#### Return Value

A new rotation. When `t=0`, the result is the `from` vector. When `t=1.0`, the result is the `to` vector. For any other value of `t`, the result is a linear linear interpolation between the two vectors.

## Parameters

- `from`: The starting vector.
- `to`: The ending vector.
- `t`: The value, between   and  , that the function interpolates at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3dfloat/lerp(from:to:t:))*