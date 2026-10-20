# init(edgeLoopFrom:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates an edge loop from a rectangle.

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
init(edgeLoopFrom rect: CGRect)
```

```objc
+ (SKPhysicsBody *) bodyWithEdgeLoopFromRect:(CGRect) rect;
```

## Mentions

- [Shaping a Physics Body to Match a Node’s Graphics](../shaping-a-physics-body-to-match-a-node-s-graphics.md)

#### Return Value

A new edge-based physics body.

#### Discussion

An edge has no volume or mass and is always treated as if the [`isDynamic`](./isdynamic.md) property is equal to [`false`](../../Swift/false.md). Edges may only collide with volume-based physics bodies.

## Parameters

- `rect`: The rectangle that defines the edges. The rectangle is specified relative to the owning node’s origin.

## See Also

### Creating an Edge-Based Physics Body
- [Creating an Edge Loop Around a Scene](../creating-an-edge-loop-around-a-scene.md)
  Border your scene with an obstacle that physics bodies cannot penetrate.
- [init(edgeFrom: CGPoint, to: CGPoint)](./init%28edgefrom,to%29.md)
  Creates an edge between two points.
- [init(edgeLoopFrom: CGPath)](./init%28edgeloopfrom%29-5grxu.md)
  Creates an edge loop from a path.
- [init(edgeChainFrom: CGPath)](./init%28edgechainfrom%29.md)
  Creates an edge chain from a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(edgeloopfrom:)-8sqfy)*