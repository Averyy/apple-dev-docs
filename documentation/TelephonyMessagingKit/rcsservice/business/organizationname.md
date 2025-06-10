# RCSService.Business.OrganizationName

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing details about a business’ name.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct OrganizationName
```

## Topics

### Accessing organization name properties
- [let displayName: String](rcsservice/business/organizationname/displayname.md)
  Display name for business.
- [let nameType: RCSService.Business.OrganizationName.NameType](rcsservice/business/organizationname/nametype-swift.property.md)
  The type of the name.
- [RCSService.Business.OrganizationName.NameType](rcsservice/business/organizationname/nametype-swift.enum.md)
  Enumeration representing the type of name specified by the business.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/organizationname/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/business/organizationname/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing organization names
- [static func == (RCSService.Business.OrganizationName, RCSService.Business.OrganizationName) -> Bool](rcsservice/business/organizationname/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/organizationname/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let description: String?](rcsservice/business/description.md)
  Description for business.
- [let providerName: String?](rcsservice/business/providername.md)
  Name of business provider.
- [let organizationNames: [RCSService.Business.OrganizationName]](rcsservice/business/organizationnames.md)
  Array of names specified by business.
- [let categoryNames: [String]](rcsservice/business/categorynames.md)
  Array of category names which can be used to filter a list of businesses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/organizationname)*