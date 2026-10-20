# vendorConfiguration

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A dictionary of provider-specific configuration settings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var vendorConfiguration: [String : Any]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,id> * vendorConfiguration;
```

#### Discussion

All of the values in this dictionary must be [`NSSecureCoding`](../../Foundation/nssecurecoding.md)-compliant.

## See Also

### Accessing the filter configuration
- [var serverAddress: String?](./serveraddress.md)
  The address of a server that the Filter Control Provider may contact for rules and other configuration information.
- [var username: String?](./username.md)
  A string that identifies the user.
- [var organization: String?](./organization.md)
  A string that identifies the organization that administers the filter.
- [var passwordReference: Data?](./passwordreference.md)
  A persistent reference to a keychain item containing a password associated with the filter.
- [var identityReference: Data?](./identityreference.md)
  A persistent reference to a keychain item containing a certificate and private key associated with the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/vendorconfiguration)*