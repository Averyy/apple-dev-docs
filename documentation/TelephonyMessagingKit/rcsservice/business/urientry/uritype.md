# RCSService.Business.URIEntry.URIType

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing the type of URI.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum URIType
```

## Topics

### Determining URI type
- [RCSService.Business.URIEntry.URIType.sip](rcsservice/business/urientry/uritype/sip.md)
  SIP URI.
- [RCSService.Business.URIEntry.URIType.other](rcsservice/business/urientry/uritype/other.md)
  Other type of URI.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/urientry/uritype/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.URIEntry.URIType, RCSService.Business.URIEntry.URIType) -> Bool](rcsservice/business/urientry/uritype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/business/urientry/uritype/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/urientry/uritype/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/business/urientry/uritype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/business/urientry/uritype/equatable-implementations.md)

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

- [let uri: URL](rcsservice/business/urientry/uri.md)
  URI provided by business.
- [let type: RCSService.Business.URIEntry.URIType](rcsservice/business/urientry/type.md)
  Type of URI.
- [let label: RCSService.Business.URIEntry.Label](rcsservice/business/urientry/label-swift.property.md)
  Label for URI.
- [RCSService.Business.URIEntry.Label](rcsservice/business/urientry/label-swift.enum.md)
  Enumeration representing the URI label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/urientry/uritype)*