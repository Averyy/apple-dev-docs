# init(origin:direction:)

**Framework**: Spatial  
**Kind**: init

Creates a ray from Spatial primitives that describe the origin and direction.

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
init(origin: Point3DFloat = .zero, direction: Vector3DFloat)
```

#### Discussion

> **Note**: This function normalizes the direction vector.

## Parameters

- `origin`: The origin of the ray.
- `direction`: The direction of the ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/init(origin:direction:)-2oe8j)*