# identityReference

**Framework**: Network Extension  
**Kind**: property

A persistent keychain reference to a keychain item containing the certificate and private key components of the tunneling protocol authentication credential.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var identityReference: Data? { get set }
```

#### Discussion

The keychain item must have the [`kSecClassIdentity`](https://developer.apple.com/documentation/Security/kSecClassIdentity) class. In macOS, the system ignores this property for [`NEVPNProtocolIPSec`](nevpnprotocolipsec.md) objects. On iOS, the system ignores this property for [`NEVPNProtocolIPSec`](nevpnprotocolipsec.md) and [`NEVPNProtocolIKEv2`](nevpnprotocolikev2.md) objects. In these cases where the system ingores this property, set the identity using the [`identityData`](nevpnprotocol/identitydata.md) property.

## See Also

- [var username: String?](nevpnprotocol/username.md)
  The user name component of the tunneling protocol authentication credential.
- [var passwordReference: Data?](nevpnprotocol/passwordreference.md)
  A persistent keychain reference to a keychain item containing the password component of the tunneling protocol authentication credential.
- [var identityData: Data?](nevpnprotocol/identitydata.md)
  The certificate and private key components of the tunneling protocol authentication credential, in PKCS12 format.
- [var identityDataPassword: String?](nevpnprotocol/identitydatapassword.md)
  The password for the PKCS12 tunneling protocol authentication credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/identityreference)*