# vertexIndex(primitive:vertex:)

**Framework**: RealityKit  
**Kind**: method

Returns the vertex index of the specified vertex within the specified primitive.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func vertexIndex(primitive: UInt32, vertex: UInt32) -> UInt32
```

#### Return Value

The vertex index of the specified vertex within the specified primitive.

## Parameters

- `primitive`: The zero-based index of the primitive.
- `vertex`: The zero-based index of the vertex within the primitive.

## See Also

- [var vertexCount: Int](clothmeshresource/vertexcount.md)
  The number of vertices in the mesh.
- [func position(at: UInt32) -> SIMD3<Float>](clothmeshresource/position(at:).md)
  Returns the position of the vertex at the given index.
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothmeshresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [func vertexIndex(at: UInt32) -> UInt32](clothmeshresource/vertexindex(at:).md)
  Returns the vertex index at the given position in the mesh’s flattened primitive index array.
- [func vertices(in: ClothVolumeShape, center: SIMD3<Float>, orientation: simd_quatf) -> [UInt32]](clothmeshresource/vertices(in:center:orientation:).md)
  Returns the indices of the vertices that lie inside the given volume shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/vertexindex(primitive:vertex:))*