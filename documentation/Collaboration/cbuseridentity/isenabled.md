# isEnabled

**Framework**: Collaboration  
**Kind**: property

Returns a Boolean value indicating whether the identity is allowed to authenticate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isEnabled: Bool { get }
```

#### Return Value

`TRUE` if the identity can authenticate; otherwise, `FALSE`.

#### Discussion

If the identity does not have authentication credentials (a password or certificate), it is not able to log in. However, an identity with authentication credentials does not ensure that it is enabled. Any identity can be disabled.

## See Also

- [func authenticate(withPassword: String) -> Bool](cbuseridentity/authenticate(withpassword:).md)
  Returns a Boolean value indicating whether the given password is correct for the identity.
- [var certificate: SecCertificate?](cbuseridentity/certificate.md)
  Returns the public authentication certificate associated with a user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbuseridentity/isenabled)*