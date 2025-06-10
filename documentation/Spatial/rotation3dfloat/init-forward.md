# init(forward:)

**Framework**: Spatial  
**Kind**: init

Returns a rotation with the specified forward vector.

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
init(forward: Vector3DFloat)
```

#### Discussion

- Parameter forward The forward direction.

> **Note**: This function creates a rotation with an up vector that’s `Vector3D(x: 0, y: 1, z: 0)` and where `+z` is forward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/init(forward:))*