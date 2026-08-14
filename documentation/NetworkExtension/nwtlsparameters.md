# NWTLSParameters

**Framework**: Network Extension  
**Kind**: class

TLS properties for creating a connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NWTLSParameters
```

## Topics

### Accessing TLS parameters
- [var tlsSessionID: Data?](nwtlsparameters/tlssessionid.md)
  The Session ID to use for the associated TCP connection.
- [var sslCipherSuites: Set<NSNumber>?](nwtlsparameters/sslciphersuites.md)
  The set of allowed cipher suites when negotiating TLS.
- [var minimumSSLProtocolVersion: Int](nwtlsparameters/minimumsslprotocolversion.md)
  The minimum allowed `SSLProtocol` value to use when negotiating TLS.
- [var maximumSSLProtocolVersion: Int](nwtlsparameters/maximumsslprotocolversion.md)
  The maximum allowed `SSLProtocol` value to use when negotiating TLS.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NWTCPConnection](nwtcpconnection.md)
  An object to manage a TCP connection, with or without TLS.
- [protocol NWTCPConnectionAuthenticationDelegate](nwtcpconnectionauthenticationdelegate.md)
  A delegate protocol to customize the TLS authentication done by a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtlsparameters)*