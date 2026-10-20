# init(polygonFrom:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a polygonal physics body.

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
init(polygonFrom path: CGPath)
```

```objc
+ (SKPhysicsBody *) bodyWithPolygonFromPath:(CGPathRef) path;
```

## Mentions

- [Shaping a Physics Body to Match a Node’s Graphics](../shaping-a-physics-body-to-match-a-node-s-graphics.md)

#### Return Value

A new volume-based physics body.

## Parameters

- `path`: A convex polygonal path with counterclockwise winding and no self intersections. The points are specified relative to the owning node’s origin.

## See Also

### Creating a Body from a Shape
- [init(circleOfRadius: CGFloat)](./init%28circleofradius%29.md)
  Creates a circular physics body centered on the owning node’s origin.
- [init(circleOfRadius: CGFloat, center: CGPoint)](./init%28circleofradius,center%29.md)
  Creates a circular physics body centered on an arbitrary point.
- [init(rectangleOf: CGSize)](./init%28rectangleof%29.md)
  Creates a rectangular physics body centered on the owning node’s origin.
- [init(rectangleOf: CGSize, center: CGPoint)](./init%28rectangleof,center%29.md)
  Creates a rectangular physics body centered on an arbitrary point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(polygonfrom:))*