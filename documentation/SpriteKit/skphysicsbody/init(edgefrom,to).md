# init(edgeFrom:to:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates an edge between two points.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(edgeFrom p1: CGPoint, to p2: CGPoint)
```

```objc
+ (SKPhysicsBody *) bodyWithEdgeFromPoint:(CGPoint) p1 toPoint:(CGPoint) p2;
```

## Mentions

- [Shaping a Physics Body to Match a Node’s Graphics](../shaping-a-physics-body-to-match-a-node-s-graphics.md)

## Return Value

A new edge-based physics body.

## Discussion

An edge has no volume or mass and is always treated as if the [`isDynamic`](./isdynamic.md) property is equal to [`false`](../../Swift/false.md). Edges may only collide with volume-based physics bodies.

## Parameters

- `p1`: The starting point for the edge, relative to the owning node’s origin.
- `p2`: The ending point for the edge, relative to the owning node’s origin.

## See Also

### Creating an Edge-Based Physics Body
- [Creating an Edge Loop Around a Scene](../creating-an-edge-loop-around-a-scene.md)
  Border your scene with an obstacle that physics bodies cannot penetrate.
- [init(edgeLoopFrom: CGRect)](./init%28edgeloopfrom%29-8sqfy.md)
  Creates an edge loop from a rectangle.
- [init(edgeLoopFrom: CGPath)](./init%28edgeloopfrom%29-5grxu.md)
  Creates an edge loop from a path.
- [init(edgeChainFrom: CGPath)](./init%28edgechainfrom%29.md)
  Creates an edge chain from a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(edgefrom:to:))*