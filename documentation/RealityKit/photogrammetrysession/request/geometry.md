# PhotogrammetrySession.Request.Geometry

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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
- [init(bounds: BoundingBox, transform: Transform)](./geometry/init%28bounds,transform%29.md)
  Creates an instance with an optional bounding box and transform.
### Accessing geometry data
- [var bounds: BoundingBox](./geometry/bounds.md)
  The bounding box for the created entity.
- [var transform: Transform](./geometry/transform.md)
  A transform applied to the created entity.
### Initializers
- [init(orientedBounds: OrientedBoundingBox, transform: Transform)](./geometry/init%28orientedbounds,transform%29.md)
  Creates an instance from an oriented bounding box and transform.
### Instance Properties
- [var orientedBounds: OrientedBoundingBox](./geometry/orientedbounds.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/geometry)*