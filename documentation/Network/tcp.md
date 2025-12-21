# TCP

**Framework**: Network  
**Kind**: struct

The system definition of the Transmission Control Protocol (TCP).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct TCP
```

#### Overview

Supports sending and receiving byte streams.

## Topics

### Initializers
- [init()](tcp/init.md)
  Create an instance of TCP.
- [init(() -> IP)](tcp/init(_:).md)
  Create an instance of TCP.
### Instance Methods
- [func ackStretchingDisabled(Bool) -> TCP](tcp/ackstretchingdisabled(_:).md)
  Disable ACK stretching.
- [func connectionTimeout(UInt32) -> TCP](tcp/connectiontimeout(_:).md)
  Set the timeout for TCP connection establishment.
- [func ecnDisabled(Bool) -> TCP](tcp/ecndisabled(_:).md)
  Disable ECN negotiation.
- [func fastOpenAllowed(Bool) -> TCP](tcp/fastopenallowed(_:).md)
  Configure TCP to enable TCP Fast Open (TFO).
- [func keepalive(idleTimeInSeconds: UInt32, count: UInt32, intervalInSeconds: UInt32) -> TCP](tcp/keepalive(idletimeinseconds:count:intervalinseconds:).md)
  Enable TCP keepalives.
- [func maximumSegmentSize(UInt32) -> TCP](tcp/maximumsegmentsize(_:).md)
  Set maximum segment size.
- [func noDelay(Bool) -> TCP](tcp/nodelay(_:).md)
  Disable Nagle’s algorithm.
- [func noOptions(Bool) -> TCP](tcp/nooptions(_:).md)
  Enable no-options mode.
- [func noPush(Bool) -> TCP](tcp/nopush(_:).md)
  Enable no-push mode.
- [func persistTimeout(UInt32) -> TCP](tcp/persisttimeout(_:).md)
  Set the TCP persist timeout.
- [func retransmitConnectionDropTime(UInt32) -> TCP](tcp/retransmitconnectiondroptime(_:).md)
  Set the TCP retransmission attempt timeout.
- [func retransmitFinDrop(Bool) -> TCP](tcp/retransmitfindrop(_:).md)
  Configure TCP to drop the connection after a FIN does not receive an ACK.

## Relationships

### Conforms To
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)
- [StreamProtocol](streamprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp)*