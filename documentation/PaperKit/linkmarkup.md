# LinkMarkup

**Framework**: PaperKit  
**Kind**: struct

A URL link that a person can tap on in the canvas.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LinkMarkup
```

## Topics

### Creating a link
- [init(url: URL, frame: CGRect, allowedInteractions: MarkupInteractions, id: MarkupID<LinkMarkup>)](linkmarkup/init(url:frame:allowedinteractions:id:).md)
  Initializes and returns a new link markup from the specified parameters.
### Accessing the destination
- [var url: URL](linkmarkup/url.md)
  The URL that the link navigates to when activated.
### Identifying markup
- [var id: MarkupID<LinkMarkup>](linkmarkup/id.md)
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
- [struct ShapeMarkup](shapemarkup.md)
  A markup element that represents a shape or text box with customizable appearance and behavior.
- [struct LoupeMarkup](loupemarkup.md)
  A loupe magnifier that magnifies the content below the loupe.
- [struct MarkupInteractions](markupinteractions.md)
  Interactions that people can perform on markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/linkmarkup)*