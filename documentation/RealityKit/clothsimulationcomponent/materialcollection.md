# ClothSimulationComponent.MaterialCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of materials.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MaterialCollection
```

## Topics

### Accessing materials
- [subscript(String, ClothBodyMaterial.Type) -> ClothBodyMaterial?](clothsimulationcomponent/materialcollection/subscript(_:_:)-49wu.md)
  Accesses a body material by name, returning `nil` if the name is absent or the material is not a body material.
- [subscript(String, ClothColliderMaterial.Type) -> ClothColliderMaterial?](clothsimulationcomponent/materialcollection/subscript(_:_:)-8ncq4.md)
  Accesses a collider material by name, returning `nil` if the name is absent or the material is not a collider material.
### Removing materials
- [func remove(name: String)](clothsimulationcomponent/materialcollection/remove(name:).md)
### Subscripts
- [subscript(String) -> ClothSimulationComponent.Material?](clothsimulationcomponent/materialcollection/subscript(_:).md)
  Accesses the material with the given name, returning `nil` if no material with that name exists.
- [subscript(_:_:)](clothsimulationcomponent/materialcollection/subscript(_:_:).md)
  Accesses a body material by name, returning `nil` if the name is absent or the material is not a body material.

## Relationships

### Conforms To
- [Collection](../swift/collection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [var materials: ClothSimulationComponent.MaterialCollection](clothsimulationcomponent/materials.md)
  A collection of materials that cloth colliders and cloth bodies can use in this simulation.
- [ClothSimulationComponent.Material](clothsimulationcomponent/material.md)
  A material that represents a cloth body or collider material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/materialcollection)*