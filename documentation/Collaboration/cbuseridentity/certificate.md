# certificate

**Framework**: Collaboration  
**Kind**: property

Returns the public authentication certificate associated with a user identity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var certificate: SecCertificate? { get }
```

#### Return Value

The public authentication certificate, or `nil` if none exists.

#### Discussion

The Collaboration framework supports certificate-based authentication in addition to passwords. If a certificate is stored for a user identity, it will be the default method of authentication.

When a .Mac account is associated with a user identity, the authentication certificate is automatically downloaded from the .Mac servers.

## See Also

- [func authenticate(withPassword: String) -> Bool](cbuseridentity/authenticate(withpassword:).md)
  Returns a Boolean value indicating whether the given password is correct for the identity.
- [var isEnabled: Bool](cbuseridentity/isenabled.md)
  Returns a Boolean value indicating whether the identity is allowed to authenticate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbuseridentity/certificate)*