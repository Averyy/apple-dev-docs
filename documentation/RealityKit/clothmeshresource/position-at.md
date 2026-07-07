# position(at:)

**Framework**: RealityKit  
**Kind**: method

Returns the position of the vertex at the given index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func position(at vertexIndex: UInt32) -> SIMD3<Float>
```

#### Return Value

The position of the specified vertex.

#### Discussion

If you want to obtain the position for a specific vertex within a specific primitive (for example the third vertex of the 20th triangle in a triangle mesh), you can use [`vertexIndex(at:)`](clothmeshresource/vertexindex(at:).md) to obtain the right vertex index:

```swift
let vertexIndex = myMesh.vertexIndex(at: 3 * 19 + 2)
let vertexPosition = myMesh.position(at: vertexIndex)
print("The third vertex of the 20th triangle is at X=\(vertexPosition.x)")
```

> ⚠️ **Warning**: This returned position corresponds to the mesh used to generate the bodies, rather than the bodies themselves. Therefore, this position does not change as the body deforms when this resource is used in [`mesh`](clothbodycomponent/mesh.md).

## Parameters

- `vertexIndex`: Index of the vertex to get the position for.

## See Also

- [var vertexCount: Int](clothmeshresource/vertexcount.md)
  The number of vertices in the mesh.
- [var positions: Span<SIMD3<Float>>](clothmeshresource/positions.md)
  The positions of all the vertices.
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothmeshresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [func vertexIndex(at: UInt32) -> UInt32](clothmeshresource/vertexindex(at:).md)
  Returns the vertex index at the given position in the mesh’s flattened primitive index array.
- [func vertexIndex(primitive: UInt32, vertex: UInt32) -> UInt32](clothmeshresource/vertexindex(primitive:vertex:).md)
  Returns the vertex index of the specified vertex within the specified primitive.
- [func vertices(in: ClothVolumeShape, center: SIMD3<Float>, orientation: simd_quatf) -> [UInt32]](clothmeshresource/vertices(in:center:orientation:).md)
  Returns the indices of the vertices that lie inside the given volume shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/position(at:))*