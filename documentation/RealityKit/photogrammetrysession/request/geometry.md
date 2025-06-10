# PhotogrammetrySession.Request.Geometry

**Framework**: RealityKit  
**Kind**: struct

An object that holds a bounding box and transformation data for a request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct Geometry
```

## Topics

### Creating a geometry instance
- [init(bounds: BoundingBox, transform: Transform)](photogrammetrysession/request/geometry/init(bounds:transform:).md)
  Creates an instance with an optional bounding box and transform.
### Accessing geometry data
- [var bounds: BoundingBox](photogrammetrysession/request/geometry/bounds.md)
  The bounding box for the created entity.
- [var transform: Transform](photogrammetrysession/request/geometry/transform.md)
  A transform applied to the created entity.
### Initializers
- [init(orientedBounds: OrientedBoundingBox, transform: Transform)](photogrammetrysession/request/geometry/init(orientedbounds:transform:).md)
  Creates an instance from an oriented bounding box and transform.
### Instance Properties
- [var orientedBounds: OrientedBoundingBox](photogrammetrysession/request/geometry/orientedbounds.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/geometry)*