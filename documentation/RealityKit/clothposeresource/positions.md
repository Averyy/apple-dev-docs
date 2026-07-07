# positions

**Framework**: RealityKit  
**Kind**: property

The positions of all the vertices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var positions: Span<SIMD3<Float>> { get }
```

#### Discussion

The span’s lifetime is tied to `self`.

## See Also

- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothposeresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [func position(at: UInt32) -> SIMD3<Float>](clothposeresource/position(at:).md)
  Returns the position of the vertex at the given index.
- [var vertexCount: Int](clothposeresource/vertexcount.md)
  The number of vertices in the pose resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothposeresource/positions)*