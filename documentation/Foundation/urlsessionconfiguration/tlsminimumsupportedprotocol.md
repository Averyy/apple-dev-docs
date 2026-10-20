# tlsMinimumSupportedProtocol

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The minimum TLS protocol to accept during protocol negotiation.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.9+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`tlsMinimumSupportedProtocolVersion`](./tlsminimumsupportedprotocolversion.md) instead.

## Declaration

```swift
var tlsMinimumSupportedProtocol: SSLProtocol { get set }
```

```objc
@property SSLProtocol TLSMinimumSupportedProtocol;
```

#### Discussion

This property determines the minimum supported TLS protocol version for tasks within sessions based on this configuration.

## See Also

### Setting security policies
- [var tlsMinimumSupportedProtocolVersion: tls_protocol_version_t](./tlsminimumsupportedprotocolversion.md)
  The minimum TLS protocol version that the client should accept when making connections in this session.
- [var tlsMaximumSupportedProtocolVersion: tls_protocol_version_t](./tlsmaximumsupportedprotocolversion.md)
  The maximum TLS protocol version that the client should request when making connections in this session.
- [var urlCredentialStorage: URLCredentialStorage?](./urlcredentialstorage.md)
  A credential store that provides credentials for authentication.
- [var tlsMaximumSupportedProtocol: SSLProtocol](./tlsmaximumsupportedprotocol.md)
  The maximum TLS protocol version that the client should request when making connections in this session.
- [var requiresDNSSECValidation: Bool](./requiresdnssecvalidation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/tlsminimumsupportedprotocol)*