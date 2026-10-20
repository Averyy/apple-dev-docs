# SSLAuthenticate

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The flags that represent the requirements for client-side authentication.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SSLAuthenticate
```

```c
enum SSLAuthenticate : int;
```

## Topics

### Constants
- [SSLAuthenticate.neverAuthenticate](./sslauthenticate/neverauthenticate.md)
  Indicates that client-side authentication is not required. (Default.)
- [SSLAuthenticate.alwaysAuthenticate](./sslauthenticate/alwaysauthenticate.md)
  Indicates that client-side authentication is required.
- [SSLAuthenticate.tryAuthenticate](./sslauthenticate/tryauthenticate.md)
  Indicates that client-side authentication should be attempted. There is no error if the client doesn’t have a certificate.
### Initializers
- [init?(rawValue: Int32)](./sslauthenticate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslauthenticate)*