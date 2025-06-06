# init(rectangleOf:center:)

**Framework**: SpriteKit  
**Kind**: init

Creates a rectangular physics body centered on an arbitrary point.

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
init(rectangleOf s: CGSize, center: CGPoint)
```

#### Return Value

A new volume-based physics body.

## Parameters

- `s`: The size of the rectangle.
- `center`: The center of the square in the owning node’s coordinate system.

## See Also

- [init(circleOfRadius: CGFloat)](skphysicsbody/init(circleofradius:).md)
  Creates a circular physics body centered on the owning node’s origin.
- [init(circleOfRadius: CGFloat, center: CGPoint)](skphysicsbody/init(circleofradius:center:).md)
  Creates a circular physics body centered on an arbitrary point.
- [init(rectangleOf: CGSize)](skphysicsbody/init(rectangleof:).md)
  Creates a rectangular physics body centered on the owning node’s origin.
- [init(polygonFrom: CGPath)](skphysicsbody/init(polygonfrom:).md)
  Creates a polygonal physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(rectangleof:center:))*