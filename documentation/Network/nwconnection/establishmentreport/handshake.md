# NWConnection.EstablishmentReport.Handshake

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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
- [let handshakeDuration: TimeInterval](./handshake/handshakeduration.md)
  The duration of the protocol handshake.
- [let handshakeRTT: TimeInterval](./handshake/handshakertt.md)
  The round-trip time the protocol observed during its handshake.
### Identifying Protocols
- [let definition: NWProtocolDefinition](./handshake/definition.md)
  The protocol performing the handshake.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting Protocol Handshakes
- [let handshakes: [NWConnection.EstablishmentReport.Handshake]](./handshakes.md)
  The array of protocol handshakes in order from first completed to last completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/handshake)*