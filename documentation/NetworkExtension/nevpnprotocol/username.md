# username

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The user name component of the tunneling protocol authentication credential.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var username: String? { get set }
```

```objc
@property (copy, nullable) NSString * username;
```

## See Also

### Authenticating the user
- [var passwordReference: Data?](./passwordreference.md)
  A persistent keychain reference to a keychain item containing the password component of the tunneling protocol authentication credential.
- [var identityReference: Data?](./identityreference.md)
  A persistent keychain reference to a keychain item containing the certificate and private key components of the tunneling protocol authentication credential.
- [var identityData: Data?](./identitydata.md)
  The certificate and private key components of the tunneling protocol authentication credential, in PKCS12 format.
- [var identityDataPassword: String?](./identitydatapassword.md)
  The password for the PKCS12 tunneling protocol authentication credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/username)*