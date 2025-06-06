# serverAddress

**Framework**: Network Extension  
**Kind**: property

The address of a server that the Filter Control Provider may contact for rules and other configuration information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var serverAddress: String? { get set }
```

## See Also

- [var vendorConfiguration: [String : Any]?](nefilterproviderconfiguration/vendorconfiguration.md)
  A dictionary of provider-specific configuration settings.
- [var username: String?](nefilterproviderconfiguration/username.md)
  A string that identifies the user.
- [var organization: String?](nefilterproviderconfiguration/organization.md)
  A string that identifies the organization that administers the filter.
- [var passwordReference: Data?](nefilterproviderconfiguration/passwordreference.md)
  A persistent reference to a keychain item containing a password associated with the filter.
- [var identityReference: Data?](nefilterproviderconfiguration/identityreference.md)
  A persistent reference to a keychain item containing a certificate and private key associated with the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/serveraddress)*