# authenticate(withPassword:)

**Framework**: Collaboration  
**Kind**: method

Returns a Boolean value indicating whether the given password is correct for the identity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func authenticate(withPassword password: String) -> Bool
```

#### Return Value

`TRUE` if the password is correct; otherwise, `FALSE`.

## Parameters

- `password`: The password to test for the identity.

## See Also

- [Identity Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004490)
- [var certificate: SecCertificate?](cbuseridentity/certificate.md)
  Returns the public authentication certificate associated with a user identity.
- [var isEnabled: Bool](cbuseridentity/isenabled.md)
  Returns a Boolean value indicating whether the identity is allowed to authenticate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbuseridentity/authenticate(withpassword:))*