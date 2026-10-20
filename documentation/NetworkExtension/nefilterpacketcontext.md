# NEFilterPacketContext

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The context object provided to the filter packet handler.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NEFilterPacketContext
```

```objc
@interface NEFilterPacketContext : NSObject
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Filtering packets
- [var packetHandler: NEFilterPacketHandler?](./nefilterpacketprovider/packethandler.md)
  A Swift closure or an ObjectiveC block that handles each packet received by the filter.
- [typealias NEFilterPacketHandler](./nefilterpackethandler.md)
  A type for Swift closures or ObjectiveC blocks that make filtering decisions about network packets.
- [enum NETrafficDirection](./netrafficdirection.md)
  A type to represent the direction of network traffic.
- [NEFilterPacketProvider.Verdict](./nefilterpacketprovider/verdict.md)
  The verdict returned by a packet handler indicating what the framework should do with a packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketcontext)*