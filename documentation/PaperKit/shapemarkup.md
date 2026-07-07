# ShapeMarkup

**Framework**: PaperKit  
**Kind**: struct

A markup element that represents a shape or text box with customizable appearance and behavior.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ShapeMarkup
```

#### Overview

Use `ShapeMarkup` to add geometric shapes, lines, and text containers to your markup content. Shapes can be filled, stroked, rotated, and configured with various visual properties.

```swift
// Create a filled rectangle
let rect = ShapeMarkup(
    shape: .rectangle,
    frame: CGRect(x: 0, y: 0, width: 100, height: 50),
    fillColor: CGColor(red: 0, green: 0, blue: 1, alpha: 1)
)

// Create a resizable textbox
var textBox = ShapeMarkup(
    shape: .rectangle,
    frame: CGRect(x: 0, y: 0, width: 80, height: 80),
    attributedText: AttributedString("Star!"),
    autoresizing: [.flexibleWidth]
)
textBox.attributedText = AttributedString("This text will cause the box to expand")

// Create an arrow line
let arrow = ShapeMarkup(
    shape: .line(start: .zero, control: CGPoint(x: 0.5, y: 0), end: CGPoint(x: 1, y: 0)),
    frame: CGRect(x: 0, y: 0, width: 200, height: 2),
    strokeColor: CGColor(red: 0, green: 0, blue: 0, alpha: 1),
    endLineMarker: .arrow
)
```

## Topics

### Creating a shape
- [init(configuration: ShapeConfiguration, frame: CGRect, rotation: CGFloat)](shapemarkup/init(configuration:frame:rotation:).md)
  Initializes and returns a new shape markup from the specified parameters.
- [init(shape: ShapeMarkup.Shape, frame: CGRect, rotation: CGFloat, fillColor: CGColor?, strokeColor: CGColor?, lineWidth: CGFloat, opacity: CGFloat, startLineMarker: ShapeMarkup.LineMarker, endLineMarker: ShapeMarkup.LineMarker, attributedText: AttributedString, allowedInteractions: MarkupInteractions, autoresizing: MarkupAutoresizing, id: MarkupID<ShapeMarkup>)](shapemarkup/init(shape:frame:rotation:fillcolor:strokecolor:linewidth:opacity:startlinemarker:endlinemarker:attributedtext:allowedinteractions:autoresizing:id:).md)
  Initializes and returns a new shape markup from the specified parameters.
### Choosing a shape type
- [var shape: ShapeMarkup.Shape](shapemarkup/shape-swift.property.md)
  The type of the shape.
- [var shapeScaled: ShapeMarkup.Shape](shapemarkup/shapescaled.md)
  The type of the shape with values scaled to the current frame.
- [ShapeMarkup.Shape](shapemarkup/shape-swift.enum.md)
### Configuring fill and stroke
- [var fillColor: CGColor?](shapemarkup/fillcolor.md)
  The color used to fill the shape’s path.
- [var strokeColor: CGColor?](shapemarkup/strokecolor.md)
  The color used to stroke the shape’s path.
- [var lineWidth: CGFloat](shapemarkup/linewidth.md)
  The line width of the shape’s path.
- [var opacity: CGFloat](shapemarkup/opacity.md)
  The opacity of the shape.
### Configuring text
- [var attributedText: AttributedString](shapemarkup/attributedtext.md)
  The attributed text displayed inside this shape.
### Configuring line markers
- [var startLineMarker: ShapeMarkup.LineMarker](shapemarkup/startlinemarker.md)
  The line marker used at the start of an open shape path.
- [var endLineMarker: ShapeMarkup.LineMarker](shapemarkup/endlinemarker.md)
  The line marker used at the end of an open shape path.
- [ShapeMarkup.LineMarker](shapemarkup/linemarker.md)
  A marker that can be attached to a line.
### Configuring sizing
- [var autoresizing: MarkupAutoresizing](shapemarkup/autoresizing.md)
  Automatic sizing behaviors for this markup.
### Identifying markup
- [var id: MarkupID<ShapeMarkup>](shapemarkup/id.md)
  Stable unique identity of the markup.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Markup](markup.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Markup](markup.md)
  A markup component.
- [struct ImageMarkup](imagemarkup.md)
  A markup element that represents an image.
- [struct LinkMarkup](linkmarkup.md)
  A URL link that a person can tap on in the canvas.
- [struct LoupeMarkup](loupemarkup.md)
  A loupe magnifier that magnifies the content below the loupe.
- [struct MarkupInteractions](markupinteractions.md)
  Interactions that people can perform on markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup)*