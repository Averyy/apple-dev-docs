# ShapeMarkup.Shape

**Framework**: PaperKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Shape
```

## Topics

### Structures
- [ShapeMarkup.Shape.ArrowShape](./shape-swift.enum/arrowshape.md)
- [ShapeMarkup.Shape.ChatBubble](./shape-swift.enum/chatbubble.md)
- [ShapeMarkup.Shape.Ellipse](./shape-swift.enum/ellipse-swift.struct.md)
- [ShapeMarkup.Shape.Line](./shape-swift.enum/line.md)
- [ShapeMarkup.Shape.Rectangle](./shape-swift.enum/rectangle-swift.struct.md)
- [ShapeMarkup.Shape.RegularPolygon](./shape-swift.enum/regularpolygon.md)
- [ShapeMarkup.Shape.Star](./shape-swift.enum/star-swift.struct.md)
### Enumeration Cases
- [case arrowShape(ShapeMarkup.Shape.ArrowShape)](./shape-swift.enum/arrowshape%28_%29.md)
  An arrow shape pointing in a specific direction.
- [case chatBubble(ShapeMarkup.Shape.ChatBubble)](./shape-swift.enum/chatbubble%28_%29.md)
  A speech bubble with a tail pointing to a specific location.
- [case ellipse(ShapeMarkup.Shape.Ellipse)](./shape-swift.enum/ellipse%28_%29.md)
  An ellipse.
- [case line(ShapeMarkup.Shape.Line)](./shape-swift.enum/line%28_%29.md)
  A quadratic Bézier curve line.
- [case rectangle(ShapeMarkup.Shape.Rectangle)](./shape-swift.enum/rectangle%28_%29.md)
  A rectangle.
- [case regularPolygon(ShapeMarkup.Shape.RegularPolygon)](./shape-swift.enum/regularpolygon%28_%29.md)
  A regular polygon with equal sides and angles.
- [case star(ShapeMarkup.Shape.Star)](./shape-swift.enum/star%28_%29.md)
  A star shape with alternating inner and outer points.
### Initializers
- [init(configurationType: ShapeConfiguration.Shape)](./shape-swift.enum/init%28configurationtype%29.md)
  Creates a default shape for a category of shape.
### Instance Properties
- [var configurationType: ShapeConfiguration.Shape](./shape-swift.enum/configurationtype.md)
  The category of shape.
- [var path: CGPath](./shape-swift.enum/path.md)
  The path of the shape.
- [var supportsLineMarkers: Bool](./shape-swift.enum/supportslinemarkers.md)
  True if this shape supports the addition of line markers.
### Type Properties
- [static var ellipse: ShapeMarkup.Shape](./shape-swift.enum/ellipse-swift.type.property.md)
  An ellipse that fills the shape’s bounds.
- [static var rectangle: ShapeMarkup.Shape](./shape-swift.enum/rectangle-swift.type.property.md)
  A rectangle with square corners.
- [static var star: ShapeMarkup.Shape](./shape-swift.enum/star-swift.type.property.md)
  A default 5-pointed star shape.
### Type Methods
- [static func arrowShape(cornerPoint: CGPoint) -> ShapeMarkup.Shape](./shape-swift.enum/arrowshape%28cornerpoint%29.md)
  An arrow shape pointing in a specific direction.
- [static func chatBubble(tailLocation: CGPoint, tailAngle: CGFloat) -> ShapeMarkup.Shape](./shape-swift.enum/chatbubble%28taillocation,tailangle%29.md)
  A speech bubble with a tail pointing to a specific location.
- [static func line(start: CGPoint, control: CGPoint?, end: CGPoint) -> ShapeMarkup.Shape](./shape-swift.enum/line%28start,control,end%29.md)
  A quadratic Bézier curve line.
- [static func regularPolygon(sides: Int) -> ShapeMarkup.Shape](./shape-swift.enum/regularpolygon%28sides%29.md)
  A regular polygon with equal sides and angles.
- [static func roundedRectangle(cornerRadius: CGFloat) -> ShapeMarkup.Shape](./shape-swift.enum/roundedrectangle%28cornerradius%29.md)
  A rectangle with rounded corners.
- [static func star(points: Int, innerRadius: CGFloat) -> ShapeMarkup.Shape](./shape-swift.enum/star%28points,innerradius%29.md)
  A star shape with alternating inner and outer points.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Choosing a shape type
- [var shape: ShapeMarkup.Shape](./shape-swift.property.md)
  The type of the shape.
- [var shapeScaled: ShapeMarkup.Shape](./shapescaled.md)
  The type of the shape with values scaled to the current frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shape-swift.enum)*