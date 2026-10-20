# username

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A string that identifies the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var username: String? { get set }
```

```objc
@property (copy, nullable) NSString * username;
```

## See Also

### Accessing the filter configuration
- [var vendorConfiguration: [String : Any]?](./vendorconfiguration.md)
  A dictionary of provider-specific configuration settings.
- [var serverAddress: String?](./serveraddress.md)
  The address of a server that the Filter Control Provider may contact for rules and other configuration information.
- [var organization: String?](./organization.md)
  A string that identifies the organization that administers the filter.
- [var passwordReference: Data?](./passwordreference.md)
  A persistent reference to a keychain item containing a password associated with the filter.
- [var identityReference: Data?](./identityreference.md)
  A persistent reference to a keychain item containing a certificate and private key associated with the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/username)*