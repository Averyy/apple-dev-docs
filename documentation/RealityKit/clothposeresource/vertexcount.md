# vertexCount

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The number of vertices in the pose resource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var vertexCount: Int { get }
```

## See Also

### Accessing pose positions
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](./withpositions%28_%29.md)
  Provides access to the positions of all the vertices within a callback.
- [func position(at: UInt32) -> SIMD3<Float>](./position%28at%29.md)
  Returns the position of the vertex at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothposeresource/vertexcount)*