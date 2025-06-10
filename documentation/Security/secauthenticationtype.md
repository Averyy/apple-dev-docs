# SecAuthenticationType

**Framework**: Security  
**Kind**: enum

The authentication type to use for an Internet password.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecAuthenticationType
```

## Topics

### Constants
- [SecAuthenticationType.NTLM](secauthenticationtype/ntlm.md)
  Specifies Windows NT LAN Manager authentication.
- [SecAuthenticationType.MSN](secauthenticationtype/msn.md)
  Specifies Microsoft Network default authentication.
- [SecAuthenticationType.DPA](secauthenticationtype/dpa.md)
  Specifies Distributed Password authentication.
- [SecAuthenticationType.RPA](secauthenticationtype/rpa.md)
  Specifies Remote Password authentication.
- [SecAuthenticationType.httpBasic](secauthenticationtype/httpbasic.md)
  Specifies HTTP Basic authentication.
- [SecAuthenticationType.httpDigest](secauthenticationtype/httpdigest.md)
  Specifies HTTP Digest Access authentication.
- [SecAuthenticationType.htmlForm](secauthenticationtype/htmlform.md)
  Specifies HTML form based authentication.
- [SecAuthenticationType.default](secauthenticationtype/default.md)
  Specifies the default authentication type.
- [SecAuthenticationType.any](secauthenticationtype/any.md)
  Specifies that any authentication type is acceptable.
### Initializers
- [init?(rawValue: FourCharCode)](secauthenticationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secauthenticationtype)*