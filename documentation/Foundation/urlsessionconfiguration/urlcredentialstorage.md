# urlCredentialStorage

**Framework**: Foundation  
**Kind**: property

A credential store that provides credentials for authentication.

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
var urlCredentialStorage: URLCredentialStorage? { get set }
```

#### Discussion

This property determines the credential storage object used by tasks within sessions based on this configuration.

If you don’t want to use a credential store, set this property to `nil`.

For default and background sessions, the default value is the [`shared`](urlcredentialstorage/shared.md) credential store object.

For [`ephemeral`](urlsessionconfiguration/ephemeral.md) sessions, the default value is a private credential store object that stores data in memory only, and is destroyed when you invalidate the session.

## See Also

- [var tlsMinimumSupportedProtocolVersion: tls_protocol_version_t](urlsessionconfiguration/tlsminimumsupportedprotocolversion.md)
  The minimum TLS protocol version that the client should accept when making connections in this session.
- [var tlsMaximumSupportedProtocolVersion: tls_protocol_version_t](urlsessionconfiguration/tlsmaximumsupportedprotocolversion.md)
  The maximum TLS protocol version that the client should request when making connections in this session.
- [var tlsMinimumSupportedProtocol: SSLProtocol](urlsessionconfiguration/tlsminimumsupportedprotocol.md)
  The minimum TLS protocol to accept during protocol negotiation.
- [var tlsMaximumSupportedProtocol: SSLProtocol](urlsessionconfiguration/tlsmaximumsupportedprotocol.md)
  The maximum TLS protocol version that the client should request when making connections in this session.
- [var requiresDNSSECValidation: Bool](urlsessionconfiguration/requiresdnssecvalidation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/urlcredentialstorage)*