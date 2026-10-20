# tlsSessionID

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The Session ID to use for the associated TCP connection.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`sec_protocol_options_set_tls_resumption_enabled(_:_:)`](../../Security/sec_protocol_options_set_tls_resumption_enabled%28_,_%29.md) function from the [Security](../../Security/Security.md) framework instead.

## Declaration

```swift
var tlsSessionID: Data? { get set }
```

```objc
@property (copy, nullable) NSData * TLSSessionID;
```

#### Discussion

The Session ID is used for TLS session resumption.

## See Also

### Accessing TLS parameters
- [var sslCipherSuites: Set<NSNumber>?](./sslciphersuites.md)
  The set of allowed cipher suites when negotiating TLS.
- [var minimumSSLProtocolVersion: Int](./minimumsslprotocolversion.md)
  The minimum allowed `SSLProtocol` value to use when negotiating TLS.
- [var maximumSSLProtocolVersion: Int](./maximumsslprotocolversion.md)
  The maximum allowed `SSLProtocol` value to use when negotiating TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtlsparameters/tlssessionid)*