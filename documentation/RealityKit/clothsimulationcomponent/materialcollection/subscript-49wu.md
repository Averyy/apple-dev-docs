# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript

Accesses a body material by name, returning `nil` if the name is absent or the material is not a body material.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
subscript(name: String, type: ClothBodyMaterial.Type) -> ClothBodyMaterial? { get set }
```

## See Also

- [subscript(String, ClothColliderMaterial.Type) -> ClothColliderMaterial?](clothsimulationcomponent/materialcollection/subscript(_:_:)-8ncq4.md)
  Accesses a collider material by name, returning `nil` if the name is absent or the material is not a collider material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/materialcollection/subscript(_:_:)-49wu)*