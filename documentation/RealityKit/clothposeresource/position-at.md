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

## Parameters

- `vertexIndex`: Index of the vertex to get the position for.

## See Also

- [var positions: Span<SIMD3<Float>>](clothposeresource/positions.md)
  The positions of all the vertices.
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothposeresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [var vertexCount: Int](clothposeresource/vertexcount.md)
  The number of vertices in the pose resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothposeresource/position(at:))*