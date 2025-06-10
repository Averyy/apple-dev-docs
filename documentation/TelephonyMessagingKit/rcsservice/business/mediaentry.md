# RCSService.Business.MediaEntry

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing media details provided by a business.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct MediaEntry
```

## Topics

### Accessing media properties
- [let label: RCSService.Business.MediaEntry.Label](rcsservice/business/mediaentry/label-swift.property.md)
  Label for media.
- [RCSService.Business.MediaEntry.Label](rcsservice/business/mediaentry/label-swift.enum.md)
  Enumeration representing the label for media.
- [let media: RCSService.Business.Media](rcsservice/business/mediaentry/media.md)
  The media contained in this entry.
- [RCSService.Business.Media](rcsservice/business/media.md)
  Structure containing media information provided by a business.
- [let contentType: RCSService.Business.MediaEntry.ContentType](rcsservice/business/mediaentry/contenttype-swift.property.md)
  Content type for media.
- [RCSService.Business.MediaEntry.ContentType](rcsservice/business/mediaentry/contenttype-swift.enum.md)
  Content type for media.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/mediaentry/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/business/mediaentry/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing media entries
- [static func == (RCSService.Business.MediaEntry, RCSService.Business.MediaEntry) -> Bool](rcsservice/business/mediaentry/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/mediaentry/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let mediaEntries: [RCSService.Business.MediaEntry]](rcsservice/business/mediaentries.md)
  Media entries provided by business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/mediaentry)*