# minimumSSLProtocolVersion

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The minimum allowed `SSLProtocol` value to use when negotiating TLS.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`sec_protocol_options_set_min_tls_protocol_version(_:_:)`](../../Security/sec_protocol_options_set_min_tls_protocol_version%28_,_%29.md) function from the [Security](../../Security/Security.md) framework instead.

## Declaration

```swift
var minimumSSLProtocolVersion: Int { get set }
```

```objc
@property (assign) NSUInteger minimumSSLProtocolVersion;
```

#### Discussion

Values for `SSLProtocol` are defined in `<Security/SecureTransport.h>`. If set to a non-zero value, the SSL handshake will not accept any protocol version less than the minimum.

## See Also

### Accessing TLS parameters
- [var tlsSessionID: Data?](./tlssessionid.md)
  The Session ID to use for the associated TCP connection.
- [var sslCipherSuites: Set<NSNumber>?](./sslciphersuites.md)
  The set of allowed cipher suites when negotiating TLS.
- [var maximumSSLProtocolVersion: Int](./maximumsslprotocolversion.md)
  The maximum allowed `SSLProtocol` value to use when negotiating TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtlsparameters/minimumsslprotocolversion)*