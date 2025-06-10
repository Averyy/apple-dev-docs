# tlsMinimumSupportedProtocol

**Framework**: Foundation  
**Kind**: property

The minimum TLS protocol to accept during protocol negotiation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var tlsMinimumSupportedProtocol: SSLProtocol { get set }
```

#### Discussion

This property determines the minimum supported TLS protocol version for tasks within sessions based on this configuration.

## See Also

- [var tlsMinimumSupportedProtocolVersion: tls_protocol_version_t](urlsessionconfiguration/tlsminimumsupportedprotocolversion.md)
  The minimum TLS protocol version that the client should accept when making connections in this session.
- [var tlsMaximumSupportedProtocolVersion: tls_protocol_version_t](urlsessionconfiguration/tlsmaximumsupportedprotocolversion.md)
  The maximum TLS protocol version that the client should request when making connections in this session.
- [var urlCredentialStorage: URLCredentialStorage?](urlsessionconfiguration/urlcredentialstorage.md)
  A credential store that provides credentials for authentication.
- [var tlsMaximumSupportedProtocol: SSLProtocol](urlsessionconfiguration/tlsmaximumsupportedprotocol.md)
  The maximum TLS protocol version that the client should request when making connections in this session.
- [var requiresDNSSECValidation: Bool](urlsessionconfiguration/requiresdnssecvalidation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/tlsminimumsupportedprotocol)*