# maximumSSLProtocolVersion

**Framework**: Network Extension  
**Kind**: property

The maximum allowed `SSLProtocol` value to use when negotiating TLS.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var maximumSSLProtocolVersion: Int { get set }
```

#### Discussion

Values for `SSLProtocol` are defined in `<Security/SecureTransport.h>`. If set to a non-zero value, the SSL handshake will not accept any protocol version greater than the maximum.

> ❗ **Important**:  This property should be used with caution, since it may limit the use of preferred SSL protocols.

## See Also

- [var tlsSessionID: Data?](nwtlsparameters/tlssessionid.md)
  The Session ID to use for the associated TCP connection.
- [var sslCipherSuites: Set<NSNumber>?](nwtlsparameters/sslciphersuites.md)
  The set of allowed cipher suites when negotiating TLS.
- [var minimumSSLProtocolVersion: Int](nwtlsparameters/minimumsslprotocolversion.md)
  The minimum allowed `SSLProtocol` value to use when negotiating TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtlsparameters/maximumsslprotocolversion)*