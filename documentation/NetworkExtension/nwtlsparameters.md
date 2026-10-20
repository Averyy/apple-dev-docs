# NWTLSParameters

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

TLS properties for creating a connection.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`sec_protocol_options_t`](../Security/sec_protocol_options_t.md) type from the [Security](../Security/Security.md) framework instead.

## Declaration

```swift
class NWTLSParameters
```

```objc
@interface NWTLSParameters : NSObject
```

## Topics

### Accessing TLS parameters
- [var tlsSessionID: Data?](./nwtlsparameters/tlssessionid.md)
  The Session ID to use for the associated TCP connection.
- [var sslCipherSuites: Set<NSNumber>?](./nwtlsparameters/sslciphersuites.md)
  The set of allowed cipher suites when negotiating TLS.
- [var minimumSSLProtocolVersion: Int](./nwtlsparameters/minimumsslprotocolversion.md)
  The minimum allowed `SSLProtocol` value to use when negotiating TLS.
- [var maximumSSLProtocolVersion: Int](./nwtlsparameters/maximumsslprotocolversion.md)
  The maximum allowed `SSLProtocol` value to use when negotiating TLS.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### TCP connections
- [class NWTCPConnection](./nwtcpconnection.md)
  An object to manage a TCP connection, with or without TLS.
- [protocol NWTCPConnectionAuthenticationDelegate](./nwtcpconnectionauthenticationdelegate.md)
  A delegate protocol to customize the TLS authentication done by a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtlsparameters)*