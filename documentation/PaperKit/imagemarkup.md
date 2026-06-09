# ImageMarkup

**Framework**: PaperKit  
**Kind**: struct

A markup element that represents an image.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ImageMarkup
```

## Topics

### Accessing image content
- [var image: CGImage?](imagemarkup/image.md)
  The image content displayed by this markup.
- [var orientation: CGImagePropertyOrientation](imagemarkup/orientation.md)
  The orientation of the image content.
- [var contentsBounds: CGRect](imagemarkup/contentsbounds.md)
  The portion of the image to display, in normalized coordinates.
### Configuring appearance
- [var opacity: CGFloat](imagemarkup/opacity.md)
  The opacity of the image.
- [var accessibilityDescription: String?](imagemarkup/accessibilitydescription.md)
  The accessibility description of the image for assistive technologies.
### Identifying markup
- [var id: MarkupID<ImageMarkup>](imagemarkup/id.md)
  Stable unique identity of the markup.
### Initializers
- [init?(image: NSImage, frame: CGRect, rotation: CGFloat, opacity: CGFloat, contentsBounds: CGRect, accessibilityDescription: String?, allowedInteractions: MarkupInteractions, id: MarkupID<ImageMarkup>)](imagemarkup/init(image:frame:rotation:opacity:contentsbounds:accessibilitydescription:allowedinteractions:id:)-1ggjv.md)
  Initializes and returns a new image markup from the specified parameters.
- [init?(image: UIImage, frame: CGRect, rotation: CGFloat, opacity: CGFloat, contentsBounds: CGRect, accessibilityDescription: String?, allowedInteractions: MarkupInteractions, id: MarkupID<ImageMarkup>)](imagemarkup/init(image:frame:rotation:opacity:contentsbounds:accessibilitydescription:allowedinteractions:id:)-8y6o9.md)
  Initializes and returns a new image markup from the specified parameters.
- [init(image: CGImage, frame: CGRect, rotation: CGFloat, orientation: CGImagePropertyOrientation, opacity: CGFloat, contentsBounds: CGRect, accessibilityDescription: String?, allowedInteractions: MarkupInteractions, id: MarkupID<ImageMarkup>)](imagemarkup/init(image:frame:rotation:orientation:opacity:contentsbounds:accessibilitydescription:allowedinteractions:id:).md)
  Initializes and returns a new image markup from the specified parameters.
### Instance Methods
- [func replaceImage(with: URL) throws](imagemarkup/replaceimage(with:)-10qzi.md)
  Replaces the contents of this image markup with an image file.
- [func replaceImage(with: CGImage)](imagemarkup/replaceimage(with:)-6eb53.md)
  Replaces the contents of this image markup with a `CGImage`.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Markup](markup.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Markup](markup.md)
  A markup component.
- [struct ShapeMarkup](shapemarkup.md)
  A markup element that represents a shape or text box with customizable appearance and behavior.
- [struct LinkMarkup](linkmarkup.md)
  A URL link that a person can tap on in the canvas.
- [struct LoupeMarkup](loupemarkup.md)
  A loupe magnifier that magnifies the content below the loupe.
- [struct MarkupInteractions](markupinteractions.md)
  Interactions that people can perform on markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/imagemarkup)*