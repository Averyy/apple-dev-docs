# NEFilterPacketProvider.Verdict

**Framework**: Network Extension  
**Kind**: enum

The verdict returned by a packet handler indicating what the framework should do with a packet.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum Verdict
```

## Topics

### Verdicts
- [NEFilterPacketProvider.Verdict.allow](nefilterpacketprovider/verdict/allow.md)
  A verdict to allow a packet.
- [NEFilterPacketProvider.Verdict.drop](nefilterpacketprovider/verdict/drop.md)
  A verdict to drop a packet.
- [NEFilterPacketProvider.Verdict.delay](nefilterpacketprovider/verdict/delay.md)
  A verdict to delay a packet until a future verdict.
### Initializers
- [init?(rawValue: Int)](nefilterpacketprovider/verdict/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var packetHandler: NEFilterPacketHandler?](nefilterpacketprovider/packethandler.md)
  A Swift closure or an ObjectiveC block that handles each packet received by the filter.
- [typealias NEFilterPacketHandler](nefilterpackethandler.md)
  A type for Swift closures or ObjectiveC blocks that make filtering decisions about network packets.
- [class NEFilterPacketContext](nefilterpacketcontext.md)
  The context object provided to the filter packet handler.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider/verdict)*