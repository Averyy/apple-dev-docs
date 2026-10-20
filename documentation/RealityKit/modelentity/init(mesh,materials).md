# init(mesh:materials:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a model entity with a particular mesh and set of materials.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency init(mesh: MeshResource, materials: [any Material] = [])
```

## Parameters

- `mesh`: A mesh that defines the geometry of the model.
- `materials`: Material resources that define the appearance of the model.

## See Also

### Creating a model
- [init()](./init%28%29.md)
  Creates a model entity.
- [init(mesh: MeshResource, materials: [any Material], collisionShape: ShapeResource, mass: Float)](./init%28mesh,materials,collisionshape,mass%29.md)
  Creates a model entity with a particular mesh, set of materials, collision shape, and mass.
- [init(mesh: MeshResource, materials: [any Material], collisionShapes: [ShapeResource], mass: Float)](./init%28mesh,materials,collisionshapes,mass%29.md)
  Creates a model entity with a particular mesh, set of materials, a composite collision shape, and mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelentity/init(mesh:materials:))*