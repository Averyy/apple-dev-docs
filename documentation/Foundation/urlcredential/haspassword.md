# hasPassword

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL hasPassword;
```

#### Discussion

This value is [`true`](../../Swift/true.md) if the receiver has a password, [`false`](../../Swift/false.md) otherwise.

This method does not attempt to retrieve the password.

If this credential’s password is stored in the user’s keychain, [`password`](./password.md) may return `nil` even if this method returns [`true`](../../Swift/true.md)—getting the password may fail, or the user may refuse access.

## See Also

### Getting credential properties
- [var user: String?](./user.md)
  The credential’s user name.
- [var certificates: [Any]](./certificates.md)
  The intermediate certificates of the credential, if it is a client certificate credential.
- [var password: String?](./password.md)
  The credential’s password.
- [var identity: SecIdentity?](./identity.md)
  The identity of this credential if it is a client certificate credential.
- [var persistence: URLCredential.Persistence](./persistence-swift.property.md)
  The credential’s persistence setting.
- [URLCredential.Persistence](./persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/haspassword)*