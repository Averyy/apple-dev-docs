# password

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The credential’s password.

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
var password: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * password;
```

#### Discussion

You should only access this property if you need the actual password value. If you only need to know if there is a password, use [`hasPassword`](./haspassword.md). Accessing this property may result in prompting the user for access—for example, if the password is stored in the user’s keychain.

## See Also

### Getting credential properties
- [var user: String?](./user.md)
  The credential’s user name.
- [var certificates: [Any]](./certificates.md)
  The intermediate certificates of the credential, if it is a client certificate credential.
- [var hasPassword: Bool](./haspassword.md)
  A Boolean value that indicates whether the credential has a password.
- [var identity: SecIdentity?](./identity.md)
  The identity of this credential if it is a client certificate credential.
- [var persistence: URLCredential.Persistence](./persistence-swift.property.md)
  The credential’s persistence setting.
- [URLCredential.Persistence](./persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/password)*