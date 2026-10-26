# sourcePosition(at:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns the source position of a vertex.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func sourcePosition(at index: Int) -> vector_float2
```

```objc
- (vector_float2) sourcePositionAtIndex:(NSInteger) index;
```

#### Return Value

The normalized position of the specified vertex in `sourcePositions`.

#### Discussion

The specified index must be between 0 and the warp geometry grid’s [`vertexCount`](./vertexcount.md) `- 1`.

## Parameters

- `index`: The index of the position vertex to query.

## See Also

### Accessing or Setting Grid Vertices
- [func destPosition(at: Int) -> vector_float2](./destposition%28at%29.md)
  Returns the destination position of a vertex.
- [func replacingByDestinationPositions(positions: [SIMD2<Float>]) -> SKWarpGeometryGrid](./replacingbydestinationpositions%28positions%29.md)
  Returns a copy of this grid, updated with the argument destination positions.
- [func replacingBySourcePositions(positions: [SIMD2<Float>]) -> SKWarpGeometryGrid](./replacingbysourcepositions%28positions%29.md)
  Returns a copy of this grid, updated with the argument source positions.
- [- gridByReplacingDestPositions:](./gridbyreplacingdestpositions_.md)
  Returns a copy of the receiver with the destination positions replaced by a specified array.
- [- gridByReplacingSourcePositions:](./gridbyreplacingsourcepositions_.md)
  Returns a copy of the receiver with the source positions replaced by a specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/sourceposition(at:))*