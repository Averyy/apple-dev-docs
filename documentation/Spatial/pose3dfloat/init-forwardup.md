# init(forward:up:)

**Framework**: Spatial  
**Kind**: init

Creates a pose with the specified forward and up vectors.

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
init(forward: Vector3DFloat, up: Vector3DFloat = Vector3DFloat(x: 0, y: 1, z: 0))
```

#### Discussion

> **Note**: This function creates a pose where `+z` is forward.

## Parameters

- `forward`: The forward direction.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3dfloat/init(forward:up:))*