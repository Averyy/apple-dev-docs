# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a collider material by name, returning `nil` if the name is absent or the material is not a collider material.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
subscript(name: String, type: ClothColliderMaterial.Type) -> ClothColliderMaterial? { get set }
```

**Other overloads**:

```swift
subscript(name: String, type: ClothBodyMaterial.Type) -> ClothBodyMaterial? { get set }
```

## See Also

### Accessing materials
- [subscript(String, ClothBodyMaterial.Type) -> ClothBodyMaterial?](./subscript%28_,_%29-49wu.md)
  Accesses a body material by name, returning `nil` if the name is absent or the material is not a body material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/materialcollection/subscript(_:_:)-8ncq4)*