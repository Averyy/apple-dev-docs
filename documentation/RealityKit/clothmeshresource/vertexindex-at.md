# vertexIndex(at:)

**Framework**: RealityKit  
**Kind**: method

Returns the vertex index at the given position in the mesh’s flattened primitive index array.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func vertexIndex(at index: UInt32) -> UInt32
```

#### Return Value

The vertex index at the specified position.

#### Discussion

The mesh is formed by triangles with three vertices each. Different triangles can share the same vertex (for example, two adjacent triangles share the two vertices joined by their common edge).

For example, if you want to retrieve the index of the second vertex in the eleventh triangle, you would use `myMesh.vertexIndex(at: 3 * 10 + 1)`. This is because each triangle is formed by three vertices, and indices start at zero, so the eleventh triangle starts at index 3 ⨉ 10. You then add one to get the second vertex within that triangle.

You can use the returned vertex index to inspect vertex properties. You can retrieve the position, for example, by using [`position(at:)`](clothmeshresource/position(at:).md):

```swift
let vertexIndex = myMesh.vertexIndex(at: 3 * 10 + 1)
let vertexPosition = myMesh.position(at: vertexIndex)
print("The second vertex of the eleventh triangle is at X=\(vertexPosition.x)")
```

- index: Index of the vertex to be retrieved within the list of vertex indices for all the mesh primitives.

## See Also

- [var vertexCount: Int](clothmeshresource/vertexcount.md)
  The number of vertices in the mesh.
- [var positions: Span<SIMD3<Float>>](clothmeshresource/positions.md)
  The positions of all the vertices.
- [func position(at: UInt32) -> SIMD3<Float>](clothmeshresource/position(at:).md)
  Returns the position of the vertex at the given index.
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothmeshresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [func vertexIndex(primitive: UInt32, vertex: UInt32) -> UInt32](clothmeshresource/vertexindex(primitive:vertex:).md)
  Returns the vertex index of the specified vertex within the specified primitive.
- [func vertices(in: ClothVolumeShape, center: SIMD3<Float>, orientation: simd_quatf) -> [UInt32]](clothmeshresource/vertices(in:center:orientation:).md)
  Returns the indices of the vertices that lie inside the given volume shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/vertexindex(at:))*