# RCSService.Business.Card.Media.Height

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration indicating the height of the media.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Height
```

## Topics

### Determining height
- [RCSService.Business.Card.Media.Height.short](rcsservice/business/card/media/height/short.md)
  Short height.
- [RCSService.Business.Card.Media.Height.medium](rcsservice/business/card/media/height/medium.md)
  Medium height.
- [RCSService.Business.Card.Media.Height.tall](rcsservice/business/card/media/height/tall.md)
  Tall height.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/card/media/height/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.Card.Media.Height, RCSService.Business.Card.Media.Height) -> Bool](rcsservice/business/card/media/height/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/business/card/media/height/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/card/media/height/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/business/card/media/height/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/business/card/media/height/equatable-implementations.md)

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

- [let url: URL](rcsservice/business/card/media/url.md)
  URL of media.
- [let contentType: UTType?](rcsservice/business/card/media/contenttype.md)
  Content type of media.
- [let fileSize: Measurement<UnitInformationStorage>](rcsservice/business/card/media/filesize.md)
  File size of media.
- [let thumbnailURL: URL?](rcsservice/business/card/media/thumbnailurl.md)
  URL of thumbnail.
- [let thumbnailContentType: UTType?](rcsservice/business/card/media/thumbnailcontenttype.md)
  Content type of thumbnail.
- [let thumbnailFileSize: Measurement<UnitInformationStorage>?](rcsservice/business/card/media/thumbnailfilesize.md)
  File size of thumbnail.
- [let displayHeight: RCSService.Business.Card.Media.Height](rcsservice/business/card/media/displayheight.md)
  The display height for media.
- [let description: String?](rcsservice/business/card/media/description.md)
  Description of media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/media/height)*