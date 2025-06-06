# init(polygonFrom:)

**Framework**: SpriteKit  
**Kind**: init

Creates a polygonal physics body.

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
init(polygonFrom path: CGPath)
```

## Mentions

- [Shaping a Physics Body to Match a Node’s Graphics](shaping-a-physics-body-to-match-a-node-s-graphics.md)

#### Return Value

A new volume-based physics body.

## Parameters

- `path`: A convex polygonal path with counterclockwise winding and no self intersections. The points are specified relative to the owning node’s origin.

## See Also

- [init(circleOfRadius: CGFloat)](skphysicsbody/init(circleofradius:).md)
  Creates a circular physics body centered on the owning node’s origin.
- [init(circleOfRadius: CGFloat, center: CGPoint)](skphysicsbody/init(circleofradius:center:).md)
  Creates a circular physics body centered on an arbitrary point.
- [init(rectangleOf: CGSize)](skphysicsbody/init(rectangleof:).md)
  Creates a rectangular physics body centered on the owning node’s origin.
- [init(rectangleOf: CGSize, center: CGPoint)](skphysicsbody/init(rectangleof:center:).md)
  Creates a rectangular physics body centered on an arbitrary point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(polygonfrom:))*