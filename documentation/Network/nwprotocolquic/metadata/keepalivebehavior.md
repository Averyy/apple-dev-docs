# NWProtocolQUIC.Metadata.KeepAliveBehavior

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

A QUIC connection keepalive behavior.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum KeepAliveBehavior
```

## Topics

### Keepalive Behaviors
- [NWProtocolQUIC.Metadata.KeepAliveBehavior.on](./keepalivebehavior/on.md)
  Keepalives are enabled with the default timeout.
- [NWProtocolQUIC.Metadata.KeepAliveBehavior.off](./keepalivebehavior/off.md)
  Keepalives are disabled.
- [NWProtocolQUIC.Metadata.KeepAliveBehavior.seconds(_:)](./keepalivebehavior/seconds%28_%29.md)
  Keepalives are enabled with a custom timeout, in seconds.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring Keepalives
- [var keepAlive: NWProtocolQUIC.Metadata.KeepAliveBehavior](./keepalive.md)
  The QUIC connection keepalive behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/metadata/keepalivebehavior)*