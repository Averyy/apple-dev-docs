# vertexCount

**Framework**: RealityKit  
**Kind**: property

The number of vertices in the pose resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var vertexCount: Int { get }
```

## See Also

- [var positions: Span<SIMD3<Float>>](clothposeresource/positions.md)
  The positions of all the vertices.
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothposeresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [func position(at: UInt32) -> SIMD3<Float>](clothposeresource/position(at:).md)
  Returns the position of the vertex at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothposeresource/vertexcount)*