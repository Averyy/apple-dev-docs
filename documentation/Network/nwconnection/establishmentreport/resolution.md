# NWConnection.EstablishmentReport.Resolution

**Framework**: Network  
**Kind**: struct

A description of a single DNS resolution step.

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
struct Resolution
```

## Topics

### Measuring Performance
- [let duration: TimeInterval](nwconnection/establishmentreport/resolution/duration.md)
  The duration of this resolution step, from when the query was issued to when the response was complete.
- [let source: NWConnection.EstablishmentReport.Resolution.Source](nwconnection/establishmentreport/resolution/source-swift.property.md)
  The source of the DNS response.
- [NWConnection.EstablishmentReport.Resolution.Source](nwconnection/establishmentreport/resolution/source-swift.enum.md)
  Sources that may provide DNS responses.
- [var dnsProtocol: NWConnection.EstablishmentReport.Resolution.DNSProtocol](nwconnection/establishmentreport/resolution/dnsprotocol-swift.property.md)
  The transport protocol your connection used for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol](nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum.md)
  A set of transport protocols connections use for DNS resolution.
### Examining Resolved Endpoints
- [let successfulEndpoint: NWEndpoint](nwconnection/establishmentreport/resolution/successfulendpoint.md)
  The resolved endpoint that led to the established connection.
- [let preferredEndpoint: NWEndpoint](nwconnection/establishmentreport/resolution/preferredendpoint.md)
  The resolved endpoint that the connection used for its first connection attempt.
- [let endpointCount: Int](nwconnection/establishmentreport/resolution/endpointcount.md)
  The number of endpoints resolved in this step.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [let resolutions: [NWConnection.EstablishmentReport.Resolution]](nwconnection/establishmentreport/resolutions.md)
  The array of resolution steps performed during connection establishment, in order from first resolved to last resolved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution)*