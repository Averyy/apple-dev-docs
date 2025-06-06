# GKBox

**Framework**: GameplayKit  
**Kind**: struct

The definition of an axis-aligned rectangular bounding volume addressed by the tree.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GKBox
```

## Topics

### Initializers
- [init()](gkbox/init.md)
- [init(boxMin: vector_float3, boxMax: vector_float3)](gkbox/init(boxmin:boxmax:).md)
### Instance Properties
- [var boxMax: vector_float3](gkbox/boxmax.md)
  The corner of the box with the highest coordinate values (in most coordinate systems, the near-upper-right corner).
- [var boxMin: vector_float3](gkbox/boxmin.md)
  The corner of the box with the lowest coordinate values (in most coordinate systems, the far-lower-left corner).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbox)*