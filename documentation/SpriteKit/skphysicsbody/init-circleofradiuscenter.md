# init(circleOfRadius:center:)

**Framework**: SpriteKit  
**Kind**: init

Creates a circular physics body centered on an arbitrary point.

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
init(circleOfRadius r: CGFloat, center: CGPoint)
```

#### Return Value

A new volume-based physics body.

## Parameters

- `r`: The radius of the circle.
- `center`: The origin of the circle in the owning node’s coordinate system.

## See Also

- [init(circleOfRadius: CGFloat)](skphysicsbody/init(circleofradius:).md)
  Creates a circular physics body centered on the owning node’s origin.
- [init(rectangleOf: CGSize)](skphysicsbody/init(rectangleof:).md)
  Creates a rectangular physics body centered on the owning node’s origin.
- [init(rectangleOf: CGSize, center: CGPoint)](skphysicsbody/init(rectangleof:center:).md)
  Creates a rectangular physics body centered on an arbitrary point.
- [init(polygonFrom: CGPath)](skphysicsbody/init(polygonfrom:).md)
  Creates a polygonal physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(circleofradius:center:))*