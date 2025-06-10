# NWProtocolQUIC.Metadata.KeepAliveBehavior

**Framework**: Network  
**Kind**: enum

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
- [NWProtocolQUIC.Metadata.KeepAliveBehavior.on](nwprotocolquic/metadata/keepalivebehavior/on.md)
  Keepalives are enabled with the default timeout.
- [NWProtocolQUIC.Metadata.KeepAliveBehavior.off](nwprotocolquic/metadata/keepalivebehavior/off.md)
  Keepalives are disabled.
- [NWProtocolQUIC.Metadata.KeepAliveBehavior.seconds(_:)](nwprotocolquic/metadata/keepalivebehavior/seconds(_:).md)
  Keepalives are enabled with a custom timeout, in seconds.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var keepAlive: NWProtocolQUIC.Metadata.KeepAliveBehavior](nwprotocolquic/metadata/keepalive.md)
  The QUIC connection keepalive behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/metadata/keepalivebehavior)*