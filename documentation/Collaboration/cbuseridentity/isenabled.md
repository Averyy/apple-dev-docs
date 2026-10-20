# isEnabled

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether the identity is allowed to authenticate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isEnabled) BOOL enabled;
```

#### Return Value

`TRUE` if the identity can authenticate; otherwise, `FALSE`.

#### Discussion

If the identity does not have authentication credentials (a password or certificate), it is not able to log in. However, an identity with authentication credentials does not ensure that it is enabled. Any identity can be disabled.

## See Also

### Password Authentication
- [func authenticate(withPassword: String) -> Bool](./authenticate%28withpassword%29.md)
  Returns a Boolean value indicating whether the given password is correct for the identity.
- [var certificate: SecCertificate?](./certificate.md)
  Returns the public authentication certificate associated with a user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbuseridentity/isenabled)*