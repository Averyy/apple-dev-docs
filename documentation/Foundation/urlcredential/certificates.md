# certificates

**Framework**: Foundation  
**Kind**: property

The intermediate certificates of the credential, if it is a client certificate credential.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var certificates: [Any] { get }
```

#### Discussion

The certificates are [`SecCertificate`](https://developer.apple.com/documentation/Security/SecCertificate) objects representing the intermediate certificates of the credential. This value is `nil` if this is not a client certificate credential or if the credential was created with no intermediate certificates.

## See Also

- [var user: String?](urlcredential/user.md)
  The credential’s user name.
- [var hasPassword: Bool](urlcredential/haspassword.md)
  A Boolean value that indicates whether the credential has a password.
- [var password: String?](urlcredential/password.md)
  The credential’s password.
- [var identity: SecIdentity?](urlcredential/identity.md)
  The identity of this credential if it is a client certificate credential.
- [var persistence: URLCredential.Persistence](urlcredential/persistence-swift.property.md)
  The credential’s persistence setting.
- [URLCredential.Persistence](urlcredential/persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/certificates)*