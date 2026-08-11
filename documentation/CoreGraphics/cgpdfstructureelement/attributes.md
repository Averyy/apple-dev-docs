# CGPDFStructureElement.Attributes

**Framework**: Core Graphics  
**Kind**: struct

The accessibility and presentation attributes of a structure element.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Attributes
```

#### Overview

The underlying tagged-PDF API accepts these attributes only at creation time, so they are supplied as a value when constructing a `CGPDFStructureElement` rather than mutated afterwards.

## Topics

### Initializers
- [init(title: String?, language: Locale.Language?, alternativeText: String?, expansionText: String?, actualText: String?)](cgpdfstructureelement/attributes/init(title:language:alternativetext:expansiontext:actualtext:).md)
### Instance Properties
- [var actualText: String?](cgpdfstructureelement/attributes/actualtext.md)
  Text that is an exact replacement for the element and its children, used when extracting the document’s contents.
- [var alternativeText: String?](cgpdfstructureelement/attributes/alternativetext.md)
  An alternate description of the element and its children, typically used for graphical content such as an image.
- [var expansionText: String?](cgpdfstructureelement/attributes/expansiontext.md)
  The expansion of an abbreviation or acronym.
- [var language: Locale.Language?](cgpdfstructureelement/attributes/language.md)
  The natural language of the element’s content, used when it differs from the document’s language.
- [var title: String?](cgpdfstructureelement/attributes/title.md)
  A human-readable title for the element. Presentational only; it should not be relied upon for accessibility.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstructureelement/attributes)*