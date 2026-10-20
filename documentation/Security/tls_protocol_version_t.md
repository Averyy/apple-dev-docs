# tls_protocol_version_t

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The collection of supported TLS and DTLS versions.

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
enum tls_protocol_version_t
```

```c
enum tls_protocol_version_t : uint16_t;
```

## Topics

### Protocol Versions
- [tls_protocol_version_t.TLSv10](./tls_protocol_version_t/tlsv10.md)
  The TLS 1.0 protocol.
- [tls_protocol_version_t.TLSv11](./tls_protocol_version_t/tlsv11.md)
  The TLS 1.1 protocol.
- [tls_protocol_version_t.TLSv12](./tls_protocol_version_t/tlsv12.md)
  The TLS 1.2 protocol.
- [tls_protocol_version_t.TLSv13](./tls_protocol_version_t/tlsv13.md)
  The TLS 1.3 protocol.
- [tls_protocol_version_t.DTLSv10](./tls_protocol_version_t/dtlsv10.md)
  The DTLS 1.0 protocol.
- [tls_protocol_version_t.DTLSv12](./tls_protocol_version_t/dtlsv12.md)
  The DTLS 1.2 protocol.
### Initializers
- [init?(rawValue: UInt16)](./tls_protocol_version_t/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/tls_protocol_version_t)*