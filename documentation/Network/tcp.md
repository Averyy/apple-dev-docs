# TCP

**Framework**: Network  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct TCP
```

## Topics

### Initializers
- [init()](tcp/init.md)
- [init(() -> IP)](tcp/init(_:).md)
### Instance Properties
- [let belowProtocol: IP](tcp/belowprotocol.md)
### Instance Methods
- [func ackStretchingDisabled(Bool) -> TCP](tcp/ackstretchingdisabled(_:).md)
- [func connectionTimeout(UInt32) -> TCP](tcp/connectiontimeout(_:).md)
- [func ecnDisabled(Bool) -> TCP](tcp/ecndisabled(_:).md)
- [func fastOpen(Bool) -> TCP](tcp/fastopen(_:).md)
- [func keepalive(idleTime: UInt32, count: UInt32, interval: UInt32) -> TCP](tcp/keepalive(idletime:count:interval:).md)
- [func maximumSegmentSize(UInt32) -> TCP](tcp/maximumsegmentsize(_:).md)
- [func noDelay(Bool) -> TCP](tcp/nodelay(_:).md)
- [func noOptions(Bool) -> TCP](tcp/nooptions(_:).md)
- [func noPush(Bool) -> TCP](tcp/nopush(_:).md)
- [func persistTimeout(UInt32) -> TCP](tcp/persisttimeout(_:).md)
- [func retransmitConnectionDropTime(UInt32) -> TCP](tcp/retransmitconnectiondroptime(_:).md)
- [func retransmitFinDrop(Bool) -> TCP](tcp/retransmitfindrop(_:).md)

## Relationships

### Conforms To
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)
- [StreamProtocol](streamprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp)*