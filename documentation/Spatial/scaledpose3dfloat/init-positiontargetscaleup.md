# init(position:target:scale:up:)

**Framework**: Spatial  
**Kind**: init

Creates a scaled pose at the specified position that’s oriented towards a look at target.

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
init(position: Point3DFloat = .zero, target: Point3DFloat, scale: Float = 1, up: Vector3DFloat = Vector3DFloat(x: 0, y: 1, z: 0))
```

#### Discussion

> **Note**: This function creates a scaled pose where `+z` is forward.

## Parameters

- `position`: The position of the scaled pose.
- `target`: The point that the scaled pose looks at.
- `scale`: The uniform scale of the scaled pose.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3dfloat/init(position:target:scale:up:))*