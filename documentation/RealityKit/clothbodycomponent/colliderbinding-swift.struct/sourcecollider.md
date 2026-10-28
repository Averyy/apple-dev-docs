# sourceCollider

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The entity containing the mesh-shaped collider that the body will bind to.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var sourceCollider: Entity?
```

## Discussion

For the binding to be successful, the entity must contain a `ClothColliderComponent` with a *mesh* collision shape.

## See Also

### Binding the collider
- [var isEnabled: Bool](./isenabled.md)
  Indicates whether the cloth body should actively bind to the mesh collider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/colliderbinding-swift.struct/sourcecollider)*