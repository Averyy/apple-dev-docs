# init(edgeLoopFrom:)

**Framework**: SpriteKit  
**Kind**: init

Creates an edge loop from a path.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(edgeLoopFrom path: CGPath)
```

## Mentions

- [Shaping a Physics Body to Match a Node’s Graphics](shaping-a-physics-body-to-match-a-node-s-graphics.md)

#### Return Value

A new edge-based physics body.

#### Discussion

If the path is not already closed, a loop is automatically created by joining the last point to the first.

An edge has no volume or mass and is always treated as if the [`isDynamic`](skphysicsbody/isdynamic.md) property is equal to [`false`](https://developer.apple.com/documentation/swift/false). Edges may only collide with volume-based physics bodies.

## Parameters

- `path`: A Core Graphics path. The points are specified relative to the owning node’s origin. The path must not intersect itself.

## See Also

- [Creating an Edge Loop Around a Scene](creating-an-edge-loop-around-a-scene.md)
  Border your scene with an obstacle that physics bodies cannot penetrate.
- [init(edgeLoopFrom: CGRect)](skphysicsbody/init(edgeloopfrom:)-8sqfy.md)
  Creates an edge loop from a rectangle.
- [init(edgeFrom: CGPoint, to: CGPoint)](skphysicsbody/init(edgefrom:to:).md)
  Creates an edge between two points.
- [init(edgeChainFrom: CGPath)](skphysicsbody/init(edgechainfrom:).md)
  Creates an edge chain from a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(edgeloopfrom:)-5grxu)*