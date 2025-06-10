# RCSService.Business.Card.ImageAlignment

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Image alignment within a card.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum ImageAlignment
```

## Topics

### Determining image alignment
- [RCSService.Business.Card.ImageAlignment.left](rcsservice/business/card/imagealignment-swift.enum/left.md)
  Left alignment.
- [RCSService.Business.Card.ImageAlignment.right](rcsservice/business/card/imagealignment-swift.enum/right.md)
  Right alignment.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/card/imagealignment-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.Card.ImageAlignment, RCSService.Business.Card.ImageAlignment) -> Bool](rcsservice/business/card/imagealignment-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/business/card/imagealignment-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/card/imagealignment-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/business/card/imagealignment-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/business/card/imagealignment-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let content: RCSService.Business.Card.Content](rcsservice/business/card/content-swift.property.md)
  Content of card.
- [RCSService.Business.Card.Content](rcsservice/business/card/content-swift.struct.md)
  Structure containing the contents of a card.
- [let titleFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/card/titlefontstyle.md)
  Style to use for title.
- [let descriptionFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/card/descriptionfontstyle.md)
  Style to use for description.
- [RCSService.Business.Card.FontStyle](rcsservice/business/card/fontstyle.md)
  Structure representing font style attributes in a card.
- [let imageAlignment: RCSService.Business.Card.ImageAlignment?](rcsservice/business/card/imagealignment-swift.property.md)
  Image alignment of card.
- [let orientation: RCSService.Business.Card.Orientation](rcsservice/business/card/orientation-swift.property.md)
  The orientation to use when displaying the card.
- [RCSService.Business.Card.Orientation](rcsservice/business/card/orientation-swift.enum.md)
  Enumeration indicating the orientation of a card.
- [let styleSheetURL: URL?](rcsservice/business/card/stylesheeturl.md)
  A URL to a CSS for the rendering of the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/imagealignment-swift.enum)*