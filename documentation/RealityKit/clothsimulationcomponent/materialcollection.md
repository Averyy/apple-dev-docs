# ClothSimulationComponent.MaterialCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collection of materials.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct MaterialCollection
```

## Topics

### Accessing materials
- [subscript(String, ClothBodyMaterial.Type) -> ClothBodyMaterial?](./materialcollection/subscript%28_,_%29-49wu.md)
  Accesses a body material by name, returning `nil` if the name is absent or the material is not a body material.
- [subscript(String, ClothColliderMaterial.Type) -> ClothColliderMaterial?](./materialcollection/subscript%28_,_%29-8ncq4.md)
  Accesses a collider material by name, returning `nil` if the name is absent or the material is not a collider material.
### Removing materials
- [func remove(name: String)](./materialcollection/remove%28name%29.md)
### Subscripts
- [subscript(String) -> ClothSimulationComponent.Material?](./materialcollection/subscript%28_%29.md)
  Accesses the material with the given name, returning `nil` if no material with that name exists.
- [subscript(_:_:)](./materialcollection/subscript%28_,_%29.md)
  Accesses a body material by name, returning `nil` if the name is absent or the material is not a body material.

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Assigning materials
- [var materials: ClothSimulationComponent.MaterialCollection](./materials.md)
  A collection of materials that cloth colliders and cloth bodies can use in this simulation.
- [ClothSimulationComponent.Material](./material.md)
  A material that represents a cloth body or collider material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/materialcollection)*