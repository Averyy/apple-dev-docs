# MarkupInteractions

**Framework**: PaperKit  
**Kind**: struct

Interactions that people can perform on markup elements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MarkupInteractions
```

#### Overview

Use `MarkupInteractions` to control which actions people can perform on markup elements. By default, all interactions are enabled (`.all`), allowing people to freely select, move, resize, rotate, style, and delete markup.

```swift
// Prevent people from deleting markup
markup.allowedInteractions = .all.subtracting(.delete)

// Allow only selection and moving
markup.allowedInteractions = [.select, .move]

// Make markup completely read-only
markup.allowedInteractions = .readOnly
```

## Topics

### Configuring interactions
- [static let rotate: MarkupInteractions](markupinteractions/rotate.md)
  Allows rotation.
- [static let resize: MarkupInteractions](markupinteractions/resize.md)
  Allows resizing.
- [static let move: MarkupInteractions](markupinteractions/move.md)
  Allows moving.
- [static let delete: MarkupInteractions](markupinteractions/delete.md)
  Allows deletion.
- [static let style: MarkupInteractions](markupinteractions/style.md)
  Allows style changes.
- [static let select: MarkupInteractions](markupinteractions/select.md)
  Allows selection.
### Using presets
- [static let all: MarkupInteractions](markupinteractions/all.md)
  All interactions enabled (default).
- [static let readOnly: MarkupInteractions](markupinteractions/readonly.md)
  Read-only: no interactions enabled.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [protocol Markup](markup.md)
  A markup component.
- [struct ImageMarkup](imagemarkup.md)
  A markup element that represents an image.
- [struct ShapeMarkup](shapemarkup.md)
  A markup element that represents a shape or text box with customizable appearance and behavior.
- [struct LinkMarkup](linkmarkup.md)
  A URL link that a person can tap on in the canvas.
- [struct LoupeMarkup](loupemarkup.md)
  A loupe magnifier that magnifies the content below the loupe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupinteractions)*