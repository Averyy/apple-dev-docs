# RCSService.Business.Card.FontStyle

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure representing font style attributes in a card.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct FontStyle
```

## Topics

### Determining font styles
- [static let italics: RCSService.Business.Card.FontStyle](rcsservice/business/card/fontstyle/italics.md)
  Italic style.
- [static let bold: RCSService.Business.Card.FontStyle](rcsservice/business/card/fontstyle/bold.md)
  Bold style.
- [static let underline: RCSService.Business.Card.FontStyle](rcsservice/business/card/fontstyle/underline.md)
  Underline style.
### Working with raw values
- [init(rawValue: Int)](rcsservice/business/card/fontstyle/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [let rawValue: Int](rcsservice/business/card/fontstyle/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [RCSService.Business.Card.FontStyle.RawValue](rcsservice/business/card/fontstyle/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Supporting types
- [RCSService.Business.Card.FontStyle.Element](rcsservice/business/card/fontstyle/element.md)
  The element type of the option set.
- [RCSService.Business.Card.FontStyle.ArrayLiteralElement](rcsservice/business/card/fontstyle/arrayliteralelement.md)
  The type of the elements of an array literal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/card/fontstyle/equatable-implementations.md)
- [OptionSet Implementations](rcsservice/business/card/fontstyle/optionset-implementations.md)
- [RawRepresentable Implementations](rcsservice/business/card/fontstyle/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](rcsservice/business/card/fontstyle/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [let content: RCSService.Business.Card.Content](rcsservice/business/card/content-swift.property.md)
  Content of card.
- [RCSService.Business.Card.Content](rcsservice/business/card/content-swift.struct.md)
  Structure containing the contents of a card.
- [let titleFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/card/titlefontstyle.md)
  Style to use for title.
- [let descriptionFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/card/descriptionfontstyle.md)
  Style to use for description.
- [let imageAlignment: RCSService.Business.Card.ImageAlignment?](rcsservice/business/card/imagealignment-swift.property.md)
  Image alignment of card.
- [RCSService.Business.Card.ImageAlignment](rcsservice/business/card/imagealignment-swift.enum.md)
  Image alignment within a card.
- [let orientation: RCSService.Business.Card.Orientation](rcsservice/business/card/orientation-swift.property.md)
  The orientation to use when displaying the card.
- [RCSService.Business.Card.Orientation](rcsservice/business/card/orientation-swift.enum.md)
  Enumeration indicating the orientation of a card.
- [let styleSheetURL: URL?](rcsservice/business/card/stylesheeturl.md)
  A URL to a CSS for the rendering of the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/fontstyle)*