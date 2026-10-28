# init(edgeChainFrom:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates an edge chain from a path.

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
init(edgeChainFrom path: CGPath)
```

```objc
+ (SKPhysicsBody *) bodyWithEdgeChainFromPath:(CGPathRef) path;
```

## Mentions

- [Shaping a Physics Body to Match a Node’s Graphics](../shaping-a-physics-body-to-match-a-node-s-graphics.md)

## Return Value

A new edge-based physics body.

## Discussion

An edge has no volume or mass and is always treated as if the [`isDynamic`](./isdynamic.md) property is equal to [`false`](../../Swift/false.md). Edges may only collide with volume-based physics bodies.

## Parameters

- `path`: A Core Graphics path. The points are specified relative to the owning node’s origin. The path must not intersect itself.

## See Also

### Creating an Edge-Based Physics Body
- [Creating an Edge Loop Around a Scene](../creating-an-edge-loop-around-a-scene.md)
  Border your scene with an obstacle that physics bodies cannot penetrate.
- [init(edgeLoopFrom: CGRect)](./init%28edgeloopfrom%29-8sqfy.md)
  Creates an edge loop from a rectangle.
- [init(edgeFrom: CGPoint, to: CGPoint)](./init%28edgefrom,to%29.md)
  Creates an edge between two points.
- [init(edgeLoopFrom: CGPath)](./init%28edgeloopfrom%29-5grxu.md)
  Creates an edge loop from a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(edgechainfrom:))*