# sslCipherSuites

**Framework**: Network Extension  
**Kind**: property

The set of allowed cipher suites when negotiating TLS.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sslCipherSuites: Set<NSNumber>? { get set }
```

#### Discussion

Values for cipher suites are defined in `<Security/CipherSuite.h>`. These values should be wrapped as [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects in a set. If this property is set to `nil`, the default cipher suites will be used.

## See Also

- [var tlsSessionID: Data?](nwtlsparameters/tlssessionid.md)
  The Session ID to use for the associated TCP connection.
- [var minimumSSLProtocolVersion: Int](nwtlsparameters/minimumsslprotocolversion.md)
  The minimum allowed `SSLProtocol` value to use when negotiating TLS.
- [var maximumSSLProtocolVersion: Int](nwtlsparameters/maximumsslprotocolversion.md)
  The maximum allowed `SSLProtocol` value to use when negotiating TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtlsparameters/sslciphersuites)*