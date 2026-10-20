# RCSService.Business.Card.Content

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing the contents of a card.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Content
```

## Topics

### Accessing content properties
- [let media: RCSService.Business.Card.Media?](./content-swift.struct/media.md)
  Media to display within card.
- [RCSService.Business.Card.Media](./media.md)
  Structure containing information about media in a card.
- [let title: String?](./content-swift.struct/title.md)
  Title of card.
- [let description: String?](./content-swift.struct/description.md)
  Description of card.
- [let suggestions: [RCSService.Business.Suggestion]](./content-swift.struct/suggestions.md)
  Suggestions provided by business.
- [RCSService.Business.Suggestion](../suggestion.md)
  Enumeration representing a suggestion from a business.

## Relationships

### Conforms To
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Accessing card properties
- [let content: RCSService.Business.Card.Content](./content-swift.property.md)
  Content of card.
- [let titleFontStyle: RCSService.Business.Card.FontStyle](./titlefontstyle.md)
  Style to use for title.
- [let descriptionFontStyle: RCSService.Business.Card.FontStyle](./descriptionfontstyle.md)
  Style to use for description.
- [RCSService.Business.Card.FontStyle](./fontstyle.md)
  Structure representing font style attributes in a card.
- [let imageAlignment: RCSService.Business.Card.ImageAlignment?](./imagealignment-swift.property.md)
  Image alignment of card.
- [RCSService.Business.Card.ImageAlignment](./imagealignment-swift.enum.md)
  Image alignment within a card.
- [let orientation: RCSService.Business.Card.Orientation](./orientation-swift.property.md)
  The orientation to use when displaying the card.
- [RCSService.Business.Card.Orientation](./orientation-swift.enum.md)
  Enumeration indicating the orientation of a card.
- [let styleSheetURL: URL?](./stylesheeturl.md)
  A URL to a CSS for the rendering of the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/content-swift.struct)*