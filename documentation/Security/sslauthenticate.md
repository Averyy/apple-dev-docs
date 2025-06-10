# SSLAuthenticate

**Framework**: Security  
**Kind**: enum

The flags that represent the requirements for client-side authentication.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SSLAuthenticate
```

## Topics

### Constants
- [SSLAuthenticate.neverAuthenticate](sslauthenticate/neverauthenticate.md)
  Indicates that client-side authentication is not required. (Default.)
- [SSLAuthenticate.alwaysAuthenticate](sslauthenticate/alwaysauthenticate.md)
  Indicates that client-side authentication is required.
- [SSLAuthenticate.tryAuthenticate](sslauthenticate/tryauthenticate.md)
  Indicates that client-side authentication should be attempted. There is no error if the client doesn’t have a certificate.
### Initializers
- [init?(rawValue: Int32)](sslauthenticate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslauthenticate)*