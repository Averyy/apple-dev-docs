# init(forward:scale:up:)

**Framework**: Spatial  
**Kind**: init

Creates a scaled pose with the specified forward and up vectors.

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
init(forward: Vector3DFloat, scale: Float = 1, up: Vector3DFloat = Vector3DFloat(x: 0, y: 1, z: 0))
```

#### Discussion

> **Note**: This function creates a scaled pose where `+z` is forward.

## Parameters

- `forward`: The forward direction.
- `scale`: The uniform scale of the scaled pose.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3dfloat/init(forward:scale:up:))*