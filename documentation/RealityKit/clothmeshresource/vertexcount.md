# vertexCount

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The number of vertices in the mesh.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var vertexCount: Int { get }
```

## See Also

### Accessing vertex data
- [func position(at: UInt32) -> SIMD3<Float>](./position%28at%29.md)
  Returns the position of the vertex at the given index.
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](./withpositions%28_%29.md)
  Provides access to the positions of all the vertices within a callback.
- [func vertexIndex(at: UInt32) -> UInt32](./vertexindex%28at%29.md)
  Returns the vertex index at the given position in the mesh’s flattened primitive index array.
- [func vertexIndex(primitive: UInt32, vertex: UInt32) -> UInt32](./vertexindex%28primitive,vertex%29.md)
  Returns the vertex index of the specified vertex within the specified primitive.
- [func vertices(in: ClothVolumeShape, center: SIMD3<Float>, orientation: simd_quatf) -> [UInt32]](./vertices%28in,center,orientation%29.md)
  Returns the indices of the vertices that lie inside the given volume shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/vertexcount)*