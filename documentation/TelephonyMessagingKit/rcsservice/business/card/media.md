# RCSService.Business.Card.Media

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing information about media in a card.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Media
```

## Topics

### Accessing card media properties
- [let url: URL](./media/url.md)
  URL of media.
- [let contentType: UTType?](./media/contenttype.md)
  Content type of media.
- [let fileSize: Measurement<UnitInformationStorage>](./media/filesize.md)
  File size of media.
- [let thumbnailURL: URL?](./media/thumbnailurl.md)
  URL of thumbnail.
- [let thumbnailContentType: UTType?](./media/thumbnailcontenttype.md)
  Content type of thumbnail.
- [let thumbnailFileSize: Measurement<UnitInformationStorage>?](./media/thumbnailfilesize.md)
  File size of thumbnail.
- [let displayHeight: RCSService.Business.Card.Media.Height](./media/displayheight.md)
  The display height for media.
- [RCSService.Business.Card.Media.Height](./media/height.md)
  Enumeration indicating the height of the media.
- [let description: String?](./media/description.md)
  Description of media.

## Relationships

### Conforms To
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [RCSService.Business.Card.Width](./width.md)
  Enumeration specifying the width of a card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/media)*