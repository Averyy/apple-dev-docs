# replacingByDestinationPositions(positions:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns a copy of this grid, updated with the argument destination positions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS
- watchOS 3.0+

## Declaration

```swift
func replacingByDestinationPositions(positions destination: [SIMD2<Float>]) -> SKWarpGeometryGrid
```

#### Return Value

A new warp geometry grid.

## See Also

### Accessing or Setting Grid Vertices
- [func destPosition(at: Int) -> vector_float2](./destposition%28at%29.md)
  Returns the destination position of a vertex.
- [func replacingBySourcePositions(positions: [SIMD2<Float>]) -> SKWarpGeometryGrid](./replacingbysourcepositions%28positions%29.md)
  Returns a copy of this grid, updated with the argument source positions.
- [func sourcePosition(at: Int) -> vector_float2](./sourceposition%28at%29.md)
  Returns the source position of a vertex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/replacingbydestinationpositions(positions:))*