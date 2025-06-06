# init(circleOfRadius:)

**Framework**: SpriteKit  
**Kind**: init

Creates a circular physics body centered on the owning node’s origin.

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
init(circleOfRadius r: CGFloat)
```

## Mentions

- [Shaping a Physics Body to Match a Node’s Graphics](shaping-a-physics-body-to-match-a-node-s-graphics.md)

#### Return Value

A new volume-based physics body.

#### Discussion

The following code shows the code that creates the physics body for a spherical or circular object. Because the physics body is attached to a sprite object, it usually needs volume. In this case, the sprite image is assumed to closely approximate a circle centered on the anchor point, so the radius of the circle is calculated and used to create the physics body.

Listing 1. A physics body for a circular sprite

If the physics body were significantly smaller than the sprite’s image, the data used to create the physics body might need to be provided by some other source, such as a property list.

## Parameters

- `r`: The radius of the circle.

## See Also

- [init(circleOfRadius: CGFloat, center: CGPoint)](skphysicsbody/init(circleofradius:center:).md)
  Creates a circular physics body centered on an arbitrary point.
- [init(rectangleOf: CGSize)](skphysicsbody/init(rectangleof:).md)
  Creates a rectangular physics body centered on the owning node’s origin.
- [init(rectangleOf: CGSize, center: CGPoint)](skphysicsbody/init(rectangleof:center:).md)
  Creates a rectangular physics body centered on an arbitrary point.
- [init(polygonFrom: CGPath)](skphysicsbody/init(polygonfrom:).md)
  Creates a polygonal physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(circleofradius:))*