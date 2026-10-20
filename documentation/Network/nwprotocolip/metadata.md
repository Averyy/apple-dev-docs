# NWProtocolIP.Metadata

**Framework**: Network  
**Kind**: class  
**Role**: Class

Per-packet IP metadata you configure when sending and receiving packets.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class Metadata
```

## Topics

### Sending IP Options
- [init()](./metadata/init%28%29.md)
  Initializes an IP packet configuration with default settings.
- [var ecn: NWProtocolIP.ECN](./metadata/ecn.md)
  A specific Explicit Congestion Notification flag value to set on an IP packet.
- [NWProtocolIP.ECN](./ecn.md)
  Flag values for Explicit Congestion Notifications in IP packets.
- [var serviceClass: NWParameters.ServiceClass](./metadata/serviceclass.md)
  A specific service class to mark on an IP packet.
### Receiving IP Packets
- [var receiveTime: UInt64](./metadata/receivetime.md)
  The time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.
### Instance Methods
- [func ecn(NWProtocolIP.ECN) -> Self](./metadata/ecn%28_%29.md)
- [func serviceClass(NWParameters.ServiceClass) -> Self](./metadata/serviceclass%28_%29.md)

## Relationships

### Inherits From
- [NWProtocolMetadata](../nwprotocolmetadata.md)
### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolip/metadata)*