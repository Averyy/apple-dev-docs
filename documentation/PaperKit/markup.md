# Markup

**Framework**: PaperKit  
**Kind**: protocol

A markup component.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol Markup : Sendable
```

#### Overview

> **Note**: This protocol is designed for PaperKit’s internal types only. Client conformance is not supported.

## Topics

### Laying out
- [var frame: CGRect](markup/frame.md)
  The element’s unrotated frame.
- [var rotation: CGFloat](markup/rotation.md)
  The element’s rotation around the center of its frame.
- [var renderFrame: CGRect](markup/renderframe.md)
  The unrotated frame that tightly fits the rendered contents of the element.
- [func applyTransform(CGAffineTransform)](markup/applytransform(_:).md)
  Transforms this element with the specified transform.
### Controlling interactions
- [var allowedInteractions: MarkupInteractions](markup/allowedinteractions.md)
  Interactions that people can perform on this markup.
- [struct MarkupInteractions](markupinteractions.md)
  Interactions that people can perform on markup elements.
### Managing feature compatibility
- [var featureSet: FeatureSet](markup/featureset.md)
  The set of features used by this markup.
- [func removeContentUnsupported(by: FeatureSet) -> Bool](markup/removecontentunsupported(by:).md)
  Removes all content not supported by the provided feature set.
### Identifying markup
- [var elementID: MarkupOrderedSet.ElementID](markup/elementid.md)
  The element identifier for use in a markup ordered set.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [ImageMarkup](imagemarkup.md)
- [LinkMarkup](linkmarkup.md)
- [LoupeMarkup](loupemarkup.md)
- [ShapeMarkup](shapemarkup.md)

## See Also

- [struct ImageMarkup](imagemarkup.md)
  A markup element that represents an image.
- [struct ShapeMarkup](shapemarkup.md)
  A markup element that represents a shape or text box with customizable appearance and behavior.
- [struct LinkMarkup](linkmarkup.md)
  A URL link that a person can tap on in the canvas.
- [struct LoupeMarkup](loupemarkup.md)
  A loupe magnifier that magnifies the content below the loupe.
- [struct MarkupInteractions](markupinteractions.md)
  Interactions that people can perform on markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup)*