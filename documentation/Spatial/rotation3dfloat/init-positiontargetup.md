# init(position:target:up:)

**Framework**: Spatial  
**Kind**: init

Returns a rotation that’s the look at direction from the eye position to the target.

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
init(position: Point3DFloat = Point3DFloat(x: 0, y: 0, z: 0), target: Point3DFloat, up: Vector3DFloat = Vector3DFloat(x: 0, y: 1, z: 0))
```

#### Discussion

> **Note**: This function creates a rotation where `+z` is forward.

## Parameters

- `position`: The eye position.
- `target`: The point that the rotation looks at.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/init(position:target:up:))*