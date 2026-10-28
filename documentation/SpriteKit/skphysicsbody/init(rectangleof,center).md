# init(rectangleOf:center:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a rectangular physics body centered on an arbitrary point.

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
init(rectangleOf s: CGSize, center: CGPoint)
```

```objc
+ (SKPhysicsBody *) bodyWithRectangleOfSize:(CGSize) s center:(CGPoint) center;
```

## Return Value

A new volume-based physics body.

## Parameters

- `s`: The size of the rectangle.
- `center`: The center of the square in the owning node’s coordinate system.

## See Also

### Creating a Body from a Shape
- [init(circleOfRadius: CGFloat)](./init%28circleofradius%29.md)
  Creates a circular physics body centered on the owning node’s origin.
- [init(circleOfRadius: CGFloat, center: CGPoint)](./init%28circleofradius,center%29.md)
  Creates a circular physics body centered on an arbitrary point.
- [init(rectangleOf: CGSize)](./init%28rectangleof%29.md)
  Creates a rectangular physics body centered on the owning node’s origin.
- [init(polygonFrom: CGPath)](./init%28polygonfrom%29.md)
  Creates a polygonal physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(rectangleof:center:))*