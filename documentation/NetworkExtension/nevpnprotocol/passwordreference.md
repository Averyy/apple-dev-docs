# passwordReference

**Framework**: Network Extension  
**Kind**: property

A persistent keychain reference to a keychain item containing the password component of the tunneling protocol authentication credential.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var passwordReference: Data? { get set }
```

#### Discussion

The keychain item must have the kSecClassGenericPassword class.

## See Also

- [var username: String?](nevpnprotocol/username.md)
  The user name component of the tunneling protocol authentication credential.
- [var identityReference: Data?](nevpnprotocol/identityreference.md)
  A persistent keychain reference to a keychain item containing the certificate and private key components of the tunneling protocol authentication credential.
- [var identityData: Data?](nevpnprotocol/identitydata.md)
  The certificate and private key components of the tunneling protocol authentication credential, in PKCS12 format.
- [var identityDataPassword: String?](nevpnprotocol/identitydatapassword.md)
  The password for the PKCS12 tunneling protocol authentication credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/passwordreference)*