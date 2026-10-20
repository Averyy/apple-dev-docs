# GKBox

**Framework**: GameplayKit  
**Kind**: struct  
**Role**: Structure

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

```c
struct GKBox;
```

## Topics

### Initializers
- [init()](./gkbox/init%28%29.md)
- [init(boxMin: vector_float3, boxMax: vector_float3)](./gkbox/init%28boxmin,boxmax%29.md)
### Instance Properties
- [var boxMax: vector_float3](./gkbox/boxmax.md)
  The corner of the box with the highest coordinate values (in most coordinate systems, the near-upper-right corner).
- [var boxMin: vector_float3](./gkbox/boxmin.md)
  The corner of the box with the lowest coordinate values (in most coordinate systems, the far-lower-left corner).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbox)*