# withPositions(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Provides access to the positions of all the vertices within a callback.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func withPositions<Result>(_ callback: (Span<SIMD3<Float>>) -> Result) -> Result
```

#### Return Value

The value returned by `callback`.

#### Discussion

The provided span is only valid for the lifetime of the callback.

## Parameters

- `callback`: A closure that receives a span over the vertex positions.

## See Also

### Accessing pose positions
- [func position(at: UInt32) -> SIMD3<Float>](./position%28at%29.md)
  Returns the position of the vertex at the given index.
- [var vertexCount: Int](./vertexcount.md)
  The number of vertices in the pose resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothposeresource/withpositions(_:))*