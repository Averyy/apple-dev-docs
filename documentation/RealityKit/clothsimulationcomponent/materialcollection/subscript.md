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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/materialcollection/subscript(_:_:))*