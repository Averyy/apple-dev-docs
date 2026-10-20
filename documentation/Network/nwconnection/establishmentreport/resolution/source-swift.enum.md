# NWConnection.EstablishmentReport.Resolution.Source

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [NWConnection.EstablishmentReport.Resolution.Source.query](./source-swift.enum/query.md)
  The DNS response was received from the network.
- [NWConnection.EstablishmentReport.Resolution.Source.cache](./source-swift.enum/cache.md)
  The DNS response was retrieved from a local cache.
- [NWConnection.EstablishmentReport.Resolution.Source.expiredCache](./source-swift.enum/expiredcache.md)
  The DNS response had expired and was retrieved from a local cache.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Measuring Performance
- [let duration: TimeInterval](./duration.md)
  The duration of this resolution step, from when the query was issued to when the response was complete.
- [let source: NWConnection.EstablishmentReport.Resolution.Source](./source-swift.property.md)
  The source of the DNS response.
- [var dnsProtocol: NWConnection.EstablishmentReport.Resolution.DNSProtocol](./dnsprotocol-swift.property.md)
  The transport protocol your connection used for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol](./dnsprotocol-swift.enum.md)
  A set of transport protocols connections use for DNS resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/source-swift.enum)*