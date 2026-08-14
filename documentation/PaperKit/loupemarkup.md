# LoupeMarkup

**Framework**: PaperKit  
**Kind**: struct

A loupe magnifier that magnifies the content below the loupe.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LoupeMarkup
```

#### Overview

The loupe magnifies the content beneath its frame within the parent markup. The loupe centers the magnified region on the center of its frame.

## Topics

### Creating a loupe
- [init(frame: CGRect, magnification: CGFloat, strokeColor: CGColor?, lineWidth: CGFloat, allowedInteractions: MarkupInteractions, id: MarkupID<LoupeMarkup>)](loupemarkup/init(frame:magnification:strokecolor:linewidth:allowedinteractions:id:).md)
  Initializes and returns a new loupe markup from the specified parameters.
### Configuring appearance
- [var magnification: CGFloat](loupemarkup/magnification.md)
  The magnification level applied to the content displayed within the loupe.
- [var strokeColor: CGColor?](loupemarkup/strokecolor.md)
  The color of the loupe’s border.
- [var lineWidth: CGFloat](loupemarkup/linewidth.md)
  The width of the loupe’s border in points.
### Identifying markup
- [var id: MarkupID<LoupeMarkup>](loupemarkup/id.md)
  Stable unique identity of the markup.

## Relationships

### Conforms To
- [Identifiable](../swift/identifiable.md)
- [Markup](markup.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol Markup](markup.md)
  A markup component.
- [struct ImageMarkup](imagemarkup.md)
  A markup element that represents an image.
- [struct ShapeMarkup](shapemarkup.md)
  A markup element that represents a shape or text box with customizable appearance and behavior.
- [struct LinkMarkup](linkmarkup.md)
  A URL link that a person can tap on in the canvas.
- [struct MarkupInteractions](markupinteractions.md)
  Interactions that people can perform on markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/loupemarkup)*