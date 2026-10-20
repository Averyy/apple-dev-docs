# identity

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The identity of this credential if it is a client certificate credential.

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
var identity: SecIdentity? { get }
```

```objc
@property (readonly, nullable) SecIdentityRef identity;
```

#### Discussion

This value is `nil` if the credential is not a client certificate credential.

## See Also

### Getting credential properties
- [var user: String?](./user.md)
  The credential’s user name.
- [var certificates: [Any]](./certificates.md)
  The intermediate certificates of the credential, if it is a client certificate credential.
- [var hasPassword: Bool](./haspassword.md)
  A Boolean value that indicates whether the credential has a password.
- [var password: String?](./password.md)
  The credential’s password.
- [var persistence: URLCredential.Persistence](./persistence-swift.property.md)
  The credential’s persistence setting.
- [URLCredential.Persistence](./persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/identity)*