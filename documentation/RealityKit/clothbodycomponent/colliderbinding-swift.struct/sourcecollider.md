# sourceCollider

**Framework**: RealityKit  
**Kind**: property

The entity containing the mesh-shaped collider that the body will bind to.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var sourceCollider: Entity?
```

#### Discussion

For the binding to be successful, the entity must contain a `ClothColliderComponent` with a *mesh* collision shape.

## See Also

- [var isEnabled: Bool](clothbodycomponent/colliderbinding-swift.struct/isenabled.md)
  Indicates whether the cloth body should actively bind to the mesh collider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/colliderbinding-swift.struct/sourcecollider)*