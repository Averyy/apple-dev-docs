# init(origin:direction:)

**Framework**: Spatial  
**Kind**: init

Creates a ray from Spatial primitives that describe the origin and direction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(origin: Point3D = .zero, direction: Vector3D)
```

#### Discussion

> **Note**: This function normalizes the direction vector.

## Parameters

- `origin`: The origin of the ray.
- `direction`: The direction of the ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d/init(origin:direction:)-63yk4)*