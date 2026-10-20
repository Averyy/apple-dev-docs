# init(circleOfRadius:center:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a circular physics body centered on an arbitrary point.

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
init(circleOfRadius r: CGFloat, center: CGPoint)
```

```objc
+ (SKPhysicsBody *) bodyWithCircleOfRadius:(CGFloat) r center:(CGPoint) center;
```

#### Return Value

A new volume-based physics body.

## Parameters

- `r`: The radius of the circle.
- `center`: The origin of the circle in the owning node’s coordinate system.

## See Also

### Creating a Body from a Shape
- [init(circleOfRadius: CGFloat)](./init%28circleofradius%29.md)
  Creates a circular physics body centered on the owning node’s origin.
- [init(rectangleOf: CGSize)](./init%28rectangleof%29.md)
  Creates a rectangular physics body centered on the owning node’s origin.
- [init(rectangleOf: CGSize, center: CGPoint)](./init%28rectangleof,center%29.md)
  Creates a rectangular physics body centered on an arbitrary point.
- [init(polygonFrom: CGPath)](./init%28polygonfrom%29.md)
  Creates a polygonal physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(circleofradius:center:))*