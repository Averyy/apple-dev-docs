# TCP

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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
- [init()](./tcp/init%28%29.md)
  Create an instance of TCP.
- [init(() -> IP)](./tcp/init%28_%29.md)
  Create an instance of TCP.
### Instance Methods
- [func ackStretchingDisabled(Bool) -> TCP](./tcp/ackstretchingdisabled%28_%29.md)
  Disable ACK stretching.
- [func connectionTimeout(UInt32) -> TCP](./tcp/connectiontimeout%28_%29.md)
  Set the timeout for TCP connection establishment.
- [func ecnDisabled(Bool) -> TCP](./tcp/ecndisabled%28_%29.md)
  Disable ECN negotiation.
- [func fastOpenAllowed(Bool) -> TCP](./tcp/fastopenallowed%28_%29.md)
  Configure TCP to enable TCP Fast Open (TFO).
- [func keepalive(idleTimeInSeconds: UInt32, count: UInt32, intervalInSeconds: UInt32) -> TCP](./tcp/keepalive%28idletimeinseconds,count,intervalinseconds%29.md)
  Enable TCP keepalives.
- [func maximumSegmentSize(UInt32) -> TCP](./tcp/maximumsegmentsize%28_%29.md)
  Set maximum segment size.
- [func noDelay(Bool) -> TCP](./tcp/nodelay%28_%29.md)
  Disable Nagle’s algorithm.
- [func noOptions(Bool) -> TCP](./tcp/nooptions%28_%29.md)
  Enable no-options mode.
- [func noPush(Bool) -> TCP](./tcp/nopush%28_%29.md)
  Enable no-push mode.
- [func persistTimeout(UInt32) -> TCP](./tcp/persisttimeout%28_%29.md)
  Set the TCP persist timeout.
- [func retransmitConnectionDropTime(UInt32) -> TCP](./tcp/retransmitconnectiondroptime%28_%29.md)
  Set the TCP retransmission attempt timeout.
- [func retransmitFinDrop(Bool) -> TCP](./tcp/retransmitfindrop%28_%29.md)
  Configure TCP to drop the connection after a FIN does not receive an ACK.

## Relationships

### Conforms To
- [NetworkProtocolOptions](./networkprotocoloptions.md)
- [OneToOneProtocol](./onetooneprotocol.md)
- [StreamProtocol](./streamprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp)*