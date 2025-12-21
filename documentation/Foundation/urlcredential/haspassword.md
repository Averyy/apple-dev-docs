# hasPassword

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the credential has a password.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hasPassword: Bool { get }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/Swift/true) if the receiver has a password, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

This method does not attempt to retrieve the password.

If this credential’s password is stored in the user’s keychain, [`password`](urlcredential/password.md) may return `nil` even if this method returns [`true`](https://developer.apple.com/documentation/Swift/true)—getting the password may fail, or the user may refuse access.

## See Also

- [var user: String?](urlcredential/user.md)
  The credential’s user name.
- [var certificates: [Any]](urlcredential/certificates.md)
  The intermediate certificates of the credential, if it is a client certificate credential.
- [var password: String?](urlcredential/password.md)
  The credential’s password.
- [var identity: SecIdentity?](urlcredential/identity.md)
  The identity of this credential if it is a client certificate credential.
- [var persistence: URLCredential.Persistence](urlcredential/persistence-swift.property.md)
  The credential’s persistence setting.
- [URLCredential.Persistence](urlcredential/persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/haspassword)*