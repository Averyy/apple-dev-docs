# RCSService.Business.OrganizationName

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing details about a business’ name.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct OrganizationName
```

## Topics

### Accessing organization name properties
- [let displayName: String](./organizationname/displayname.md)
  Display name for business.
- [let nameType: RCSService.Business.OrganizationName.NameType](./organizationname/nametype-swift.property.md)
  The type of the name.
- [RCSService.Business.OrganizationName.NameType](./organizationname/nametype-swift.enum.md)
  Enumeration representing the type of name specified by the business.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing business identity information
- [let description: String?](./description.md)
  Description for business.
- [let providerName: String?](./providername.md)
  Name of business provider.
- [let organizationNames: [RCSService.Business.OrganizationName]](./organizationnames.md)
  Array of names specified by business.
- [let categoryNames: [String]](./categorynames.md)
  Array of category names which can be used to filter a list of businesses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/organizationname)*