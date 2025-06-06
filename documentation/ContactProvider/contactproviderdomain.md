# ContactProviderDomain

**Framework**: ContactProvider  
**Kind**: protocol

A domain, including traits like an identifier and display name, used to configure the extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol ContactProviderDomain
```

## Topics

### Identifying the domain
- [var displayName: String](contactproviderdomain/displayname.md)
  The display name the system shows to represent this domain.
- [var identifier: String](contactproviderdomain/identifier.md)
  The identifier of the domain.
### Providing custom domain data
- [var userInfo: Dictionary<String, Any>](contactproviderdomain/userinfo.md)
  Custom values used to configure the extension before enumeration begins.

## Relationships

### Conforming Types
- [DefaultContactProviderDomain](defaultcontactproviderdomain.md)

## See Also

- [struct DefaultContactProviderDomain](defaultcontactproviderdomain.md)
  The default domain the extension uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactproviderdomain)*