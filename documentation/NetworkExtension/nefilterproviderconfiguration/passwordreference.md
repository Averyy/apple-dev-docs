# passwordReference

**Framework**: Network Extension  
**Kind**: property

A persistent reference to a keychain item containing a password associated with the filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var passwordReference: Data? { get set }
```

## See Also

- [var vendorConfiguration: [String : Any]?](nefilterproviderconfiguration/vendorconfiguration.md)
  A dictionary of provider-specific configuration settings.
- [var serverAddress: String?](nefilterproviderconfiguration/serveraddress.md)
  The address of a server that the Filter Control Provider may contact for rules and other configuration information.
- [var username: String?](nefilterproviderconfiguration/username.md)
  A string that identifies the user.
- [var organization: String?](nefilterproviderconfiguration/organization.md)
  A string that identifies the organization that administers the filter.
- [var identityReference: Data?](nefilterproviderconfiguration/identityreference.md)
  A persistent reference to a keychain item containing a certificate and private key associated with the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/passwordreference)*