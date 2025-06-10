# RCSService.Business.Card.Content

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing the contents of a card.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct Content
```

## Topics

### Accessing content properties
- [let media: RCSService.Business.Card.Media?](rcsservice/business/card/content-swift.struct/media.md)
  Media to display within card.
- [RCSService.Business.Card.Media](rcsservice/business/card/media.md)
  Structure containing information about media in a card.
- [let title: String?](rcsservice/business/card/content-swift.struct/title.md)
  Title of card.
- [let description: String?](rcsservice/business/card/content-swift.struct/description.md)
  Description of card.
- [let suggestions: [RCSService.Business.Suggestion]](rcsservice/business/card/content-swift.struct/suggestions.md)
  Suggestions provided by business.
- [RCSService.Business.Suggestion](rcsservice/business/suggestion.md)
  Enumeration representing a suggestion from a business.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/card/content-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/business/card/content-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing content instances
- [static func == (RCSService.Business.Card.Content, RCSService.Business.Card.Content) -> Bool](rcsservice/business/card/content-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/card/content-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let content: RCSService.Business.Card.Content](rcsservice/business/card/content-swift.property.md)
  Content of card.
- [let titleFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/card/titlefontstyle.md)
  Style to use for title.
- [let descriptionFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/card/descriptionfontstyle.md)
  Style to use for description.
- [RCSService.Business.Card.FontStyle](rcsservice/business/card/fontstyle.md)
  Structure representing font style attributes in a card.
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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/content-swift.struct)*