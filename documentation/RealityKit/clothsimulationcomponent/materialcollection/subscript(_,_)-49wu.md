# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a body material by name, returning `nil` if the name is absent or the material is not a body material.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
subscript(name: String, type: ClothBodyMaterial.Type) -> ClothBodyMaterial? { get set }
```

**Other overloads**:

```swift
subscript(name: String, type: ClothColliderMaterial.Type) -> ClothColliderMaterial? { get set }
```

## See Also

### Accessing materials
- [subscript(String, ClothColliderMaterial.Type) -> ClothColliderMaterial?](./subscript%28_,_%29-8ncq4.md)
  Accesses a collider material by name, returning `nil` if the name is absent or the material is not a collider material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/materialcollection/subscript(_:_:)-49wu)*