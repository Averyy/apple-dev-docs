# bias

**Framework**: RealityKit  
**Kind**: property

The distance by which the vertices are extended outwards along the direction of their normals.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var bias: Float
```

#### Discussion

This can be used to make a mesh collider slightly larger than its visual counterpart in order to avoid z-fighting.

## See Also

- [var mesh: ClothMeshResource](clothmeshshape/mesh.md)
  The mesh resource that this shape is based off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshshape/bias)*