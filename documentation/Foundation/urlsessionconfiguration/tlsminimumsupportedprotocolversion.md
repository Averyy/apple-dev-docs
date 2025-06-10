# tlsMinimumSupportedProtocolVersion

**Framework**: Foundation  
**Kind**: property

The minimum TLS protocol version that the client should accept when making connections in this session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var tlsMinimumSupportedProtocolVersion: tls_protocol_version_t { get set }
```

## See Also

- [var tlsMaximumSupportedProtocolVersion: tls_protocol_version_t](urlsessionconfiguration/tlsmaximumsupportedprotocolversion.md)
  The maximum TLS protocol version that the client should request when making connections in this session.
- [var urlCredentialStorage: URLCredentialStorage?](urlsessionconfiguration/urlcredentialstorage.md)
  A credential store that provides credentials for authentication.
- [var tlsMinimumSupportedProtocol: SSLProtocol](urlsessionconfiguration/tlsminimumsupportedprotocol.md)
  The minimum TLS protocol to accept during protocol negotiation.
- [var tlsMaximumSupportedProtocol: SSLProtocol](urlsessionconfiguration/tlsmaximumsupportedprotocol.md)
  The maximum TLS protocol version that the client should request when making connections in this session.
- [var requiresDNSSECValidation: Bool](urlsessionconfiguration/requiresdnssecvalidation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/tlsminimumsupportedprotocolversion)*