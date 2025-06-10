# RCSService.Business.MediaEntry.Label

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing the label for media.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Label
```

## Topics

### Determining label type
- [RCSService.Business.MediaEntry.Label.icon](rcsservice/business/mediaentry/label-swift.enum/icon.md)
  Icon label.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/mediaentry/label-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.MediaEntry.Label, RCSService.Business.MediaEntry.Label) -> Bool](rcsservice/business/mediaentry/label-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/business/mediaentry/label-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/mediaentry/label-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/business/mediaentry/label-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/business/mediaentry/label-swift.enum/equatable-implementations.md)

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
- [let media: RCSService.Business.Media](rcsservice/business/mediaentry/media.md)
  The media contained in this entry.
- [RCSService.Business.Media](rcsservice/business/media.md)
  Structure containing media information provided by a business.
- [let contentType: RCSService.Business.MediaEntry.ContentType](rcsservice/business/mediaentry/contenttype-swift.property.md)
  Content type for media.
- [RCSService.Business.MediaEntry.ContentType](rcsservice/business/mediaentry/contenttype-swift.enum.md)
  Content type for media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/mediaentry/label-swift.enum)*