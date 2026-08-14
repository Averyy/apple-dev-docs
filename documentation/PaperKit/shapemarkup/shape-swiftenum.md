# ShapeMarkup.Shape

**Framework**: PaperKit  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Shape
```

## Topics

### Structures
- [ShapeMarkup.Shape.ArrowShape](shapemarkup/shape-swift.enum/arrowshape.md)
- [ShapeMarkup.Shape.ChatBubble](shapemarkup/shape-swift.enum/chatbubble.md)
- [ShapeMarkup.Shape.Ellipse](shapemarkup/shape-swift.enum/ellipse-swift.struct.md)
- [ShapeMarkup.Shape.Line](shapemarkup/shape-swift.enum/line.md)
- [ShapeMarkup.Shape.Rectangle](shapemarkup/shape-swift.enum/rectangle-swift.struct.md)
- [ShapeMarkup.Shape.RegularPolygon](shapemarkup/shape-swift.enum/regularpolygon.md)
- [ShapeMarkup.Shape.Star](shapemarkup/shape-swift.enum/star-swift.struct.md)
### Enumeration Cases
- [case arrowShape(ShapeMarkup.Shape.ArrowShape)](shapemarkup/shape-swift.enum/arrowshape(_:).md)
  An arrow shape pointing in a specific direction.
- [case chatBubble(ShapeMarkup.Shape.ChatBubble)](shapemarkup/shape-swift.enum/chatbubble(_:).md)
  A speech bubble with a tail pointing to a specific location.
- [case ellipse(ShapeMarkup.Shape.Ellipse)](shapemarkup/shape-swift.enum/ellipse(_:).md)
  An ellipse.
- [case line(ShapeMarkup.Shape.Line)](shapemarkup/shape-swift.enum/line(_:).md)
  A quadratic Bézier curve line.
- [case rectangle(ShapeMarkup.Shape.Rectangle)](shapemarkup/shape-swift.enum/rectangle(_:).md)
  A rectangle.
- [case regularPolygon(ShapeMarkup.Shape.RegularPolygon)](shapemarkup/shape-swift.enum/regularpolygon(_:).md)
  A regular polygon with equal sides and angles.
- [case star(ShapeMarkup.Shape.Star)](shapemarkup/shape-swift.enum/star(_:).md)
  A star shape with alternating inner and outer points.
### Initializers
- [init(configurationType: ShapeConfiguration.Shape)](shapemarkup/shape-swift.enum/init(configurationtype:).md)
  Creates a default shape for a category of shape.
### Instance Properties
- [var configurationType: ShapeConfiguration.Shape](shapemarkup/shape-swift.enum/configurationtype.md)
  The category of shape.
- [var path: CGPath](shapemarkup/shape-swift.enum/path.md)
  The path of the shape.
- [var supportsLineMarkers: Bool](shapemarkup/shape-swift.enum/supportslinemarkers.md)
  True if this shape supports the addition of line markers.
### Type Properties
- [static var ellipse: ShapeMarkup.Shape](shapemarkup/shape-swift.enum/ellipse-swift.type.property.md)
  An ellipse that fills the shape’s bounds.
- [static var rectangle: ShapeMarkup.Shape](shapemarkup/shape-swift.enum/rectangle-swift.type.property.md)
  A rectangle with square corners.
- [static var star: ShapeMarkup.Shape](shapemarkup/shape-swift.enum/star-swift.type.property.md)
  A default 5-pointed star shape.
### Type Methods
- [static func arrowShape(cornerPoint: CGPoint) -> ShapeMarkup.Shape](shapemarkup/shape-swift.enum/arrowshape(cornerpoint:).md)
  An arrow shape pointing in a specific direction.
- [static func chatBubble(tailLocation: CGPoint, tailAngle: CGFloat) -> ShapeMarkup.Shape](shapemarkup/shape-swift.enum/chatbubble(taillocation:tailangle:).md)
  A speech bubble with a tail pointing to a specific location.
- [static func line(start: CGPoint, control: CGPoint?, end: CGPoint) -> ShapeMarkup.Shape](shapemarkup/shape-swift.enum/line(start:control:end:).md)
  A quadratic Bézier curve line.
- [static func regularPolygon(sides: Int) -> ShapeMarkup.Shape](shapemarkup/shape-swift.enum/regularpolygon(sides:).md)
  A regular polygon with equal sides and angles.
- [static func roundedRectangle(cornerRadius: CGFloat) -> ShapeMarkup.Shape](shapemarkup/shape-swift.enum/roundedrectangle(cornerradius:).md)
  A rectangle with rounded corners.
- [static func star(points: Int, innerRadius: CGFloat) -> ShapeMarkup.Shape](shapemarkup/shape-swift.enum/star(points:innerradius:).md)
  A star shape with alternating inner and outer points.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var shape: ShapeMarkup.Shape](shapemarkup/shape-swift.property.md)
  The type of the shape.
- [var shapeScaled: ShapeMarkup.Shape](shapemarkup/shapescaled.md)
  The type of the shape with values scaled to the current frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shape-swift.enum)*