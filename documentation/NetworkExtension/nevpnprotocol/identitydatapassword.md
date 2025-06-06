# identityDataPassword

**Framework**: Network Extension  
**Kind**: property

The password for the PKCS12 tunneling protocol authentication credentials.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var identityDataPassword: String? { get set }
```

#### Discussion

If the PKCS12 data set in the [`identityData`](nevpnprotocol/identitydata.md) property uses a password for encryption, you must specify the password here.

## See Also

- [var username: String?](nevpnprotocol/username.md)
  The user name component of the tunneling protocol authentication credential.
- [var passwordReference: Data?](nevpnprotocol/passwordreference.md)
  A persistent keychain reference to a keychain item containing the password component of the tunneling protocol authentication credential.
- [var identityReference: Data?](nevpnprotocol/identityreference.md)
  A persistent keychain reference to a keychain item containing the certificate and private key components of the tunneling protocol authentication credential.
- [var identityData: Data?](nevpnprotocol/identitydata.md)
  The certificate and private key components of the tunneling protocol authentication credential, in PKCS12 format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/identitydatapassword)*