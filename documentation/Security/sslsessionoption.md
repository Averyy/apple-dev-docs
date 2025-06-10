# SSLSessionOption

**Framework**: Security  
**Kind**: enum

The options that can be set for an SSL session.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SSLSessionOption
```

#### Overview

Use these flags with calls to the [`SSLSetSessionOption(_:_:_:)`](sslsetsessionoption(_:_:_:).md) function.

## Topics

### Constants
- [SSLSessionOption.breakOnServerAuth](sslsessionoption/breakonserverauth.md)
  Enables returning from [`SSLHandshake(_:)`](sslhandshake(_:).md) (with a result of `errSSLServerAuthCompleted`) when the server authentication portion of the handshake is complete to allow your application to perform its own certificate verification.
- [SSLSessionOption.breakOnCertRequested](sslsessionoption/breakoncertrequested.md)
  Enables returning from [`SSLHandshake(_:)`](sslhandshake(_:).md) (with a result of `errSSLClientCertRequested`) when the server requests a client certificate.
- [SSLSessionOption.breakOnClientAuth](sslsessionoption/breakonclientauth.md)
  Enables returning from [`SSLHandshake(_:)`](sslhandshake(_:).md) (with a result of `errSSLClientAuthCompleted`) when the client authentication portion of the handshake is complete to allow your application to perform its own certificate verification.
- [SSLSessionOption.falseStart](sslsessionoption/falsestart.md)
  When enabled, TLS False Start is used if an adequate cipher-suite is negotiated.
- [SSLSessionOption.sendOneByteRecord](sslsessionoption/sendonebyterecord.md)
  Enables `1/n-1` record splitting for BEAST attack mitigation.
- [SSLSessionOption.allowServerIdentityChange](sslsessionoption/allowserveridentitychange.md)
  Allow server identity change on renegotiation.
- [SSLSessionOption.fallback](sslsessionoption/fallback.md)
  Enable fallback countermeasures.
- [SSLSessionOption.breakOnClientHello](sslsessionoption/breakonclienthello.md)
  Break from a client hello in order to check for SNI.
- [SSLSessionOption.allowRenegotiation](sslsessionoption/allowrenegotiation.md)
  Allow renegotiation.
- [SSLSessionOption.enableSessionTickets](sslsessionoption/enablesessiontickets.md)
  Enable session tickets.
### Initializers
- [init?(rawValue: Int32)](sslsessionoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsessionoption)*