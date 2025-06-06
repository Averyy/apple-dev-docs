# minimumSSLProtocolVersion

**Framework**: Network Extension  
**Kind**: property

The minimum allowed `SSLProtocol` value to use when negotiating TLS.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var minimumSSLProtocolVersion: Int { get set }
```

#### Discussion

Values for `SSLProtocol` are defined in `<Security/SecureTransport.h>`. If set to a non-zero value, the SSL handshake will not accept any protocol version less than the minimum.

## See Also

- [var tlsSessionID: Data?](nwtlsparameters/tlssessionid.md)
  The Session ID to use for the associated TCP connection.
- [var sslCipherSuites: Set<NSNumber>?](nwtlsparameters/sslciphersuites.md)
  The set of allowed cipher suites when negotiating TLS.
- [var maximumSSLProtocolVersion: Int](nwtlsparameters/maximumsslprotocolversion.md)
  The maximum allowed `SSLProtocol` value to use when negotiating TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtlsparameters/minimumsslprotocolversion)*