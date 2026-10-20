# NEFilterPacketProvider.Verdict

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

The verdict returned by a packet handler indicating what the framework should do with a packet.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum Verdict
```

```c
enum NEFilterPacketProviderVerdict : NSInteger;
```

## Topics

### Verdicts
- [NEFilterPacketProvider.Verdict.allow](./verdict/allow.md)
  A verdict to allow a packet.
- [NEFilterPacketProvider.Verdict.drop](./verdict/drop.md)
  A verdict to drop a packet.
- [NEFilterPacketProvider.Verdict.delay](./verdict/delay.md)
  A verdict to delay a packet until a future verdict.
### Initializers
- [init?(rawValue: Int)](./verdict/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Filtering packets
- [var packetHandler: NEFilterPacketHandler?](./packethandler.md)
  A Swift closure or an ObjectiveC block that handles each packet received by the filter.
- [typealias NEFilterPacketHandler](../nefilterpackethandler.md)
  A type for Swift closures or ObjectiveC blocks that make filtering decisions about network packets.
- [class NEFilterPacketContext](../nefilterpacketcontext.md)
  The context object provided to the filter packet handler.
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider/verdict)*