# NWConnection.EstablishmentReport.Handshake

**Framework**: Network  
**Kind**: struct

A description of a single protocol handshake.

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
struct Handshake
```

## Topics

### Measuring Performance
- [let handshakeDuration: TimeInterval](nwconnection/establishmentreport/handshake/handshakeduration.md)
  The duration of the protocol handshake.
- [let handshakeRTT: TimeInterval](nwconnection/establishmentreport/handshake/handshakertt.md)
  The round-trip time the protocol observed during its handshake.
### Identifying Protocols
- [let definition: NWProtocolDefinition](nwconnection/establishmentreport/handshake/definition.md)
  The protocol performing the handshake.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let handshakes: [NWConnection.EstablishmentReport.Handshake]](nwconnection/establishmentreport/handshakes.md)
  The array of protocol handshakes in order from first completed to last completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/handshake)*