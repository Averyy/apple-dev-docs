# NWConnection.EstablishmentReport.Resolution.Source

**Framework**: Network  
**Kind**: enum

Sources that may provide DNS responses.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum Source
```

## Topics

### Resolution Sources
- [NWConnection.EstablishmentReport.Resolution.Source.query](nwconnection/establishmentreport/resolution/source-swift.enum/query.md)
  The DNS response was received from the network.
- [NWConnection.EstablishmentReport.Resolution.Source.cache](nwconnection/establishmentreport/resolution/source-swift.enum/cache.md)
  The DNS response was retrieved from a local cache.
- [NWConnection.EstablishmentReport.Resolution.Source.expiredCache](nwconnection/establishmentreport/resolution/source-swift.enum/expiredcache.md)
  The DNS response had expired and was retrieved from a local cache.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let duration: TimeInterval](nwconnection/establishmentreport/resolution/duration.md)
  The duration of this resolution step, from when the query was issued to when the response was complete.
- [let source: NWConnection.EstablishmentReport.Resolution.Source](nwconnection/establishmentreport/resolution/source-swift.property.md)
  The source of the DNS response.
- [var dnsProtocol: NWConnection.EstablishmentReport.Resolution.DNSProtocol](nwconnection/establishmentreport/resolution/dnsprotocol-swift.property.md)
  The transport protocol your connection used for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol](nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum.md)
  A set of transport protocols connections use for DNS resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/source-swift.enum)*