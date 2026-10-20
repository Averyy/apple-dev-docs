# init(mesh:bias:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a cloth collider component with a mesh shape built from the given mesh resource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(mesh: ClothMeshResource, bias: Float)
```

## Parameters

- `mesh`: Defines the mesh resource to use for the shape of the collider.
- `bias`: The distance by which the mesh vertices are extended outwards along the direction of their normals.

## See Also

### Creating a cloth collider
- [init(shape: ClothColliderShape)](./init%28shape%29.md)
  Creates a cloth collider component with the given shape.
- [init(meshShape: ClothMeshShape)](./init%28meshshape%29.md)
  Creates a cloth collider component with the given mesh shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidercomponent/init(mesh:bias:))*