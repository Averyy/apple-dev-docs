# RCSService.Business.URIEntry.Label

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing the URI label.

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
- [RCSService.Business.URIEntry.Label.serviceID](rcsservice/business/urientry/label-swift.enum/serviceid.md)
  Service ID label.
- [RCSService.Business.URIEntry.Label.sms](rcsservice/business/urientry/label-swift.enum/sms.md)
  SMS label.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/urientry/label-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.URIEntry.Label, RCSService.Business.URIEntry.Label) -> Bool](rcsservice/business/urientry/label-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/business/urientry/label-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/urientry/label-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/business/urientry/label-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/business/urientry/label-swift.enum/equatable-implementations.md)

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
- [RCSService.Business.URIEntry.URIType](rcsservice/business/urientry/uritype.md)
  Enumeration representing the type of URI.
- [let label: RCSService.Business.URIEntry.Label](rcsservice/business/urientry/label-swift.property.md)
  Label for URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/urientry/label-swift.enum)*