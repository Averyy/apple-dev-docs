# GKQuad

**Framework**: GameplayKit  
**Kind**: struct

The definition of an axis-aligned rectangle addressed by the tree.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GKQuad
```

## Topics

### Initializers
- [init()](gkquad/init.md)
- [init(quadMin: vector_float2, quadMax: vector_float2)](gkquad/init(quadmin:quadmax:).md)
### Instance Properties
- [var quadMax: vector_float2](gkquad/quadmax.md)
  The corner of the rectangle with the highest coordinate values (in most coordinate systems, the upper-right corner).
- [var quadMin: vector_float2](gkquad/quadmin.md)
  The corner of the rectangle with the lowest coordinate values (in most coordinate systems, the lower-left corner).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkquad)*