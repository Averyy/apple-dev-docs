# init(mesh:bias:)

**Framework**: RealityKit  
**Kind**: init

Creates a cloth collider component with a mesh shape built from the given mesh resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(mesh: ClothMeshResource, bias: Float)
```

## Parameters

- `mesh`: Defines the mesh resource to use for the shape of the collider.
- `bias`: The distance by which the mesh vertices are extended outwards along the direction of their normals.

## See Also

- [init(shape: ClothColliderShape)](clothcollidercomponent/init(shape:).md)
  Creates a cloth collider component with the given shape.
- [init(meshShape: ClothMeshShape)](clothcollidercomponent/init(meshshape:).md)
  Creates a cloth collider component with the given mesh shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidercomponent/init(mesh:bias:))*