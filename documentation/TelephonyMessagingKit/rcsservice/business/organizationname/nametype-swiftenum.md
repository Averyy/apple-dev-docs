# RCSService.Business.OrganizationName.NameType

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing the type of name specified by the business.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum NameType
```

## Topics

### Determining name type
- [RCSService.Business.OrganizationName.NameType.officialName](rcsservice/business/organizationname/nametype-swift.enum/officialname.md)
  Official name.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/organizationname/nametype-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.OrganizationName.NameType, RCSService.Business.OrganizationName.NameType) -> Bool](rcsservice/business/organizationname/nametype-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/business/organizationname/nametype-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/organizationname/nametype-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/business/organizationname/nametype-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/business/organizationname/nametype-swift.enum/equatable-implementations.md)

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

- [let displayName: String](rcsservice/business/organizationname/displayname.md)
  Display name for business.
- [let nameType: RCSService.Business.OrganizationName.NameType](rcsservice/business/organizationname/nametype-swift.property.md)
  The type of the name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/organizationname/nametype-swift.enum)*