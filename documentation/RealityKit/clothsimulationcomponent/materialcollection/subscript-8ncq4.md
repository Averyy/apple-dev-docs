# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript

Accesses a collider material by name, returning `nil` if the name is absent or the material is not a collider material.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
subscript(name: String, type: ClothColliderMaterial.Type) -> ClothColliderMaterial? { get set }
```

## See Also

- [subscript(String, ClothBodyMaterial.Type) -> ClothBodyMaterial?](clothsimulationcomponent/materialcollection/subscript(_:_:)-49wu.md)
  Accesses a body material by name, returning `nil` if the name is absent or the material is not a body material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/materialcollection/subscript(_:_:)-8ncq4)*