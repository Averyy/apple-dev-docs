# dnsProtocol

**Framework**: Network  
**Kind**: property

The transport protocol your connection used for DNS resolution.

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
var dnsProtocol: NWConnection.EstablishmentReport.Resolution.DNSProtocol { get }
```

## See Also

- [let duration: TimeInterval](nwconnection/establishmentreport/resolution/duration.md)
  The duration of this resolution step, from when the query was issued to when the response was complete.
- [let source: NWConnection.EstablishmentReport.Resolution.Source](nwconnection/establishmentreport/resolution/source-swift.property.md)
  The source of the DNS response.
- [NWConnection.EstablishmentReport.Resolution.Source](nwconnection/establishmentreport/resolution/source-swift.enum.md)
  Sources that may provide DNS responses.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol](nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum.md)
  A set of transport protocols connections use for DNS resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/dnsprotocol-swift.property)*