# withPositions(_:)

**Framework**: RealityKit  
**Kind**: method

Provides access to the positions of all the vertices within a callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func withPositions<Result>(_ callback: (Span<SIMD3<Float>>) -> Result) -> Result
```

#### Return Value

The value returned by `callback`.

#### Discussion

The provided span is only valid for the lifetime of the callback.

> ⚠️ **Warning**: These positions correspond to the mesh used to generate the bodies, rather than the bodies themselves. Therefore, these positions do not change as the body deforms when this resource is used in [`mesh`](clothbodycomponent/mesh.md).

## Parameters

- `callback`: A closure that receives a span over the vertex positions.

## See Also

- [var vertexCount: Int](clothmeshresource/vertexcount.md)
  The number of vertices in the mesh.
- [var positions: Span<SIMD3<Float>>](clothmeshresource/positions.md)
  The positions of all the vertices.
- [func position(at: UInt32) -> SIMD3<Float>](clothmeshresource/position(at:).md)
  Returns the position of the vertex at the given index.
- [func vertexIndex(at: UInt32) -> UInt32](clothmeshresource/vertexindex(at:).md)
  Returns the vertex index at the given position in the mesh’s flattened primitive index array.
- [func vertexIndex(primitive: UInt32, vertex: UInt32) -> UInt32](clothmeshresource/vertexindex(primitive:vertex:).md)
  Returns the vertex index of the specified vertex within the specified primitive.
- [func vertices(in: ClothVolumeShape, center: SIMD3<Float>, orientation: simd_quatf) -> [UInt32]](clothmeshresource/vertices(in:center:orientation:).md)
  Returns the indices of the vertices that lie inside the given volume shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/withpositions(_:))*