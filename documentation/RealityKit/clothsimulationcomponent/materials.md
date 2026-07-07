# materials

**Framework**: RealityKit  
**Kind**: property

A collection of materials that cloth colliders and cloth bodies can use in this simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var materials: ClothSimulationComponent.MaterialCollection
```

#### Discussion

Cloth bodies and colliders can refer to these materials by specifying the material name via [`materialNames`](clothbodycomponent/materialnames.md) and [`materialNames`](clothcollidercomponent/materialnames.md).

## See Also

- [ClothSimulationComponent.MaterialCollection](clothsimulationcomponent/materialcollection.md)
  A collection of materials.
- [ClothSimulationComponent.Material](clothsimulationcomponent/material.md)
  A material that represents a cloth body or collider material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/materials)*