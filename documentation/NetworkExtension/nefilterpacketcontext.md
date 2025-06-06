# NEFilterPacketContext

**Framework**: Network Extension  
**Kind**: class

The context object provided to the filter packet handler.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NEFilterPacketContext
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var packetHandler: NEFilterPacketHandler?](nefilterpacketprovider/packethandler.md)
  A Swift closure or an ObjectiveC block that handles each packet received by the filter.
- [typealias NEFilterPacketHandler](nefilterpackethandler.md)
  A type for Swift closures or ObjectiveC blocks that make filtering decisions about network packets.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.
- [NEFilterPacketProvider.Verdict](nefilterpacketprovider/verdict.md)
  The verdict returned by a packet handler indicating what the framework should do with a packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketcontext)*