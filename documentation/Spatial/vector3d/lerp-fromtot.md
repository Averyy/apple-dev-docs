# lerp(from:to:t:)

**Framework**: Spatial  
**Kind**: method

Returns a Spatial vector that represents the linear interpolation at `t` between two vectors.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func lerp(from: Vector3D, to: Vector3D, t: Vector3D) -> Vector3D
```

#### Return Value

A new rotation. When `t=0`, the result is the `from` vector. When `t=1.0`, the result is the `to` vector. For any other value of `t`, the result is a linear linear interpolation between the two vectors.

## Parameters

- `from`: The starting vector.
- `to`: The ending vector.
- `t`: The value, between   and  , that the function interpolates at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3d/lerp(from:to:t:))*