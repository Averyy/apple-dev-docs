# UDP

**Framework**: Network  
**Kind**: struct

The system definition of the User Datagram Protocol (UDP).

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
struct UDP
```

#### Overview

UDP supports sending and receiving datagrams.

## Topics

### Initializers
- [init()](udp/init.md)
- [init(() -> IP)](udp/init(_:).md)
### Instance Methods
- [func noChecksumPreferred(Bool) -> UDP](udp/nochecksumpreferred(_:).md)
  Skip computing checksums when sending UDP packets.

## Relationships

### Conforms To
- [DatagramProtocol](datagramprotocol.md)
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/udp)*