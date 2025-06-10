# RCSService.Business.MediaEntry.ContentType

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Content type for media.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum ContentType
```

## Topics

### Determining content type
- [RCSService.Business.MediaEntry.ContentType.logo](rcsservice/business/mediaentry/contenttype-swift.enum/logo.md)
  Logo content type.
- [RCSService.Business.MediaEntry.ContentType.other](rcsservice/business/mediaentry/contenttype-swift.enum/other.md)
  Other content type.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/mediaentry/contenttype-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.MediaEntry.ContentType, RCSService.Business.MediaEntry.ContentType) -> Bool](rcsservice/business/mediaentry/contenttype-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/business/mediaentry/contenttype-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/mediaentry/contenttype-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/business/mediaentry/contenttype-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/business/mediaentry/contenttype-swift.enum/equatable-implementations.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/mediaentry/contenttype-swift.enum)*