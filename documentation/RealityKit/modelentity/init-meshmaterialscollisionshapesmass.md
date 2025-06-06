# init(mesh:materials:collisionShapes:mass:)

**Framework**: RealityKit  
**Kind**: init

Creates a model entity with a particular mesh, set of materials, a composite collision shape, and mass.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(mesh: MeshResource, materials: [any Material] = [], collisionShapes: [ShapeResource], mass: Float)
```

## Parameters

- `mesh`: A mesh that defines the geometry of the model.
- `materials`: Material resources that define the appearance of the model.
- `collisionShapes`: A collection of shape resources that define a composite collision shape.
- `mass`: The mass of the model in kilograms.

## See Also

- [init()](modelentity/init.md)
  Creates a model entity.
- [init(mesh: MeshResource, materials: [any Material])](modelentity/init(mesh:materials:).md)
  Creates a model entity with a particular mesh and set of materials.
- [init(mesh: MeshResource, materials: [any Material], collisionShape: ShapeResource, mass: Float)](modelentity/init(mesh:materials:collisionshape:mass:).md)
  Creates a model entity with a particular mesh, set of materials, collision shape, and mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelentity/init(mesh:materials:collisionshapes:mass:))*