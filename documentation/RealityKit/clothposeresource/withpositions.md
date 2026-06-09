# withPositions(_:)

**Framework**: RealityKit  
**Kind**: method

Provides access to the positions of all the vertices within a callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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

- [var positions: Span<SIMD3<Float>>](clothposeresource/positions.md)
  The positions of all the vertices.
- [func position(at: UInt32) -> SIMD3<Float>](clothposeresource/position(at:).md)
  Returns the position of the vertex at the given index.
- [var vertexCount: Int](clothposeresource/vertexcount.md)
  The number of vertices in the pose resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothposeresource/withpositions(_:))*