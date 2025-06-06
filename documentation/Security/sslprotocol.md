# SSLProtocol

**Framework**: Security  
**Kind**: enum

An enumeration of valid SSL protocol versions.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SSLProtocol
```

#### Overview

The descriptions given here apply to the functions [`SSLSetProtocolVersion`](sslsetprotocolversion.md) and [`SSLGetProtocolVersion`](sslgetprotocolversion.md). For the functions [`SSLSetProtocolVersionEnabled`](sslsetprotocolversionenabled.md) and [`SSLGetProtocolVersionEnabled`](sslgetprotocolversionenabled.md), only the following values are used. For these functions, each constant except [`SSLProtocol.sslProtocolAll`](sslprotocol/sslprotocolall.md) specifies a single protocol version.

- [`SSLProtocol.sslProtocol2`](sslprotocol/sslprotocol2.md)
- [`SSLProtocol.sslProtocol3`](sslprotocol/sslprotocol3.md)
- [`SSLProtocol.tlsProtocol1`](sslprotocol/tlsprotocol1.md)
- [`SSLProtocol.sslProtocolAll`](sslprotocol/sslprotocolall.md)

## Topics

### SSL Protocols
- [SSLProtocol.sslProtocolUnknown](sslprotocol/sslprotocolunknown.md)
  Specifies that no protocol has been or should be negotiated or specified; use default.
- [SSLProtocol.sslProtocol2](sslprotocol/sslprotocol2.md)
  Specifies that only the SSL 2.0 protocol may be negotiated. Deprecated in iOS.
- [SSLProtocol.sslProtocol3](sslprotocol/sslprotocol3.md)
  Specifies that the SSL 3.0 protocol is preferred; the SSL 2.0 protocol may be negotiated if the peer cannot use the SSL 3.0 protocol.
- [SSLProtocol.sslProtocol3Only](sslprotocol/sslprotocol3only.md)
  Specifies that only the SSL 3.0 protocol may be negotiated; fails if the peer tries to negotiate the SSL 2.0 protocol. Deprecated in iOS.
- [SSLProtocol.sslProtocolAll](sslprotocol/sslprotocolall.md)
  Specifies all supported versions. Deprecated in iOS.
### TLS Protocols
- [SSLProtocol.tlsProtocol1](sslprotocol/tlsprotocol1.md)
  Specifies that the TLS 1.0 protocol is preferred but lower versions may be negotiated.
- [SSLProtocol.tlsProtocol1Only](sslprotocol/tlsprotocol1only.md)
  Specifies that only the TLS 1.0 protocol may be negotiated. Deprecated in iOS.
- [SSLProtocol.tlsProtocol11](sslprotocol/tlsprotocol11.md)
  Specifies that the TLS 1.1 protocol is preferred but lower versions may be negotiated.
- [SSLProtocol.tlsProtocol12](sslprotocol/tlsprotocol12.md)
  Specifies that the TLS 1.2 protocol is preferred but lower versions may be negotiated.
- [SSLProtocol.tlsProtocol13](sslprotocol/tlsprotocol13.md)
  Specifies that the TLS 1.3 protocol is preferred but lower versions may be negotiated.
- [SSLProtocol.tlsProtocolMaxSupported](sslprotocol/tlsprotocolmaxsupported.md)
  The maximum system supported version.
### DTLS Protocols
- [SSLProtocol.dtlsProtocol1](sslprotocol/dtlsprotocol1.md)
  Specifies the DTLS 1.0 protocol.
- [SSLProtocol.dtlsProtocol12](sslprotocol/dtlsprotocol12.md)
  Specifies the DTLS 1.2 protocol.
### Initializers
- [init?(rawValue: Int32)](sslprotocol/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslprotocol)*