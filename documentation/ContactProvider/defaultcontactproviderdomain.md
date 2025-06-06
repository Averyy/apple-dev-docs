# DefaultContactProviderDomain

**Framework**: ContactProvider  
**Kind**: struct

The default domain the extension uses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct DefaultContactProviderDomain
```

## Topics

### Creating a default domain
- [init()](defaultcontactproviderdomain/init.md)
  Creates an instance of the default domain.
### Identifying the domain
- [let displayName: String](defaultcontactproviderdomain/displayname.md)
  The display name the system shows to represent the default domain.
- [var identifier: String](defaultcontactproviderdomain/identifier-swift.property.md)
  The identifier of the domain.
### Providing custom domain data
- [let userInfo: Dictionary<String, Any>](defaultcontactproviderdomain/userinfo.md)
  Custom values used to configure the extension before enumeration begins.
### Using the default domain identifier
- [static let identifier: String](defaultcontactproviderdomain/identifier-swift.type.property.md)
  The identifier used for all default domains.

## Relationships

### Conforms To
- [ContactProviderDomain](contactproviderdomain.md)

## See Also

- [protocol ContactProviderDomain](contactproviderdomain.md)
  A domain, including traits like an identifier and display name, used to configure the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/defaultcontactproviderdomain)*