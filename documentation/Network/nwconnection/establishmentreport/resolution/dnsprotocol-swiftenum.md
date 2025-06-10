# NWConnection.EstablishmentReport.Resolution.DNSProtocol

**Framework**: Network  
**Kind**: enum

A set of transport protocols connections use for DNS resolution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum DNSProtocol
```

## Topics

### Resolution Transports
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.unknown](nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum/unknown.md)
  The DNS response protocol is unknown or not applicable.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.udp](nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum/udp.md)
  The connection used cleartext UDP for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.tcp](nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum/tcp.md)
  The connection used cleartext TCP for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.tls](nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum/tls.md)
  The connection used TLS for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.https](nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum/https.md)
  The connection used HTTPS for DNS resolution.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let duration: TimeInterval](nwconnection/establishmentreport/resolution/duration.md)
  The duration of this resolution step, from when the query was issued to when the response was complete.
- [let source: NWConnection.EstablishmentReport.Resolution.Source](nwconnection/establishmentreport/resolution/source-swift.property.md)
  The source of the DNS response.
- [NWConnection.EstablishmentReport.Resolution.Source](nwconnection/establishmentreport/resolution/source-swift.enum.md)
  Sources that may provide DNS responses.
- [var dnsProtocol: NWConnection.EstablishmentReport.Resolution.DNSProtocol](nwconnection/establishmentreport/resolution/dnsprotocol-swift.property.md)
  The transport protocol your connection used for DNS resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum)*