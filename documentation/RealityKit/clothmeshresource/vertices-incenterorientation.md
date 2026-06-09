# vertices(in:center:orientation:)

**Framework**: RealityKit  
**Kind**: method

Returns the indices of the vertices that lie inside the given volume shape.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func vertices(in shape: ClothVolumeShape, center: SIMD3<Float> = SIMD3<Float>(repeating: 0), orientation: simd_quatf = simd_quatf(ix: 0, iy: 0, iz: 0, r: 1)) -> [UInt32]
```

#### Return Value

The indices of the vertices that lie inside the shape.

## Parameters

- `shape`: The volume shape to test vertices against.
- `center`: The center position of the shape.
- `orientation`: The orientation of the shape.

## See Also

- [var vertexCount: Int](clothmeshresource/vertexcount.md)
  The number of vertices in the mesh.
- [var positions: Span<SIMD3<Float>>](clothmeshresource/positions.md)
  The positions of all the vertices.
- [func position(at: UInt32) -> SIMD3<Float>](clothmeshresource/position(at:).md)
  Returns the position of the vertex at the given index.
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothmeshresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [func vertexIndex(at: UInt32) -> UInt32](clothmeshresource/vertexindex(at:).md)
  Returns the vertex index at the given position in the mesh’s flattened primitive index array.
- [func vertexIndex(primitive: UInt32, vertex: UInt32) -> UInt32](clothmeshresource/vertexindex(primitive:vertex:).md)
  Returns the vertex index of the specified vertex within the specified primitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/vertices(in:center:orientation:))*