# position

**Framework**: GameplayKit  
**Kind**: property

The position of the node in continuous 2D space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var position: vector_float2 { get set }
```

#### Discussion

You specify a position when creating a node, but you can also change a node’s position after initialization.

When working with an array of nodes returned by the [`GKGraph`](gkgraph.md) [`findPath(from:to:)`](gkgraph/findpath(from:to:).md) method, read the position from each node to determine the path for an entity in your game scene to follow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode2d/position)*