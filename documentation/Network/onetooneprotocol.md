# OneToOneProtocol

**Framework**: Network  
**Kind**: protocol

Types that conform to OneToOneProtocol are allowed to be the top protocol in a network protocol stack for non-multiplexed connections.

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
protocol OneToOneProtocol : NetworkProtocolOptions
```

## Relationships

### Inherits From
- [NetworkProtocolOptions](networkprotocoloptions.md)
### Inherited By
- [DatagramProtocol](datagramprotocol.md)
- [MessageProtocol](messageprotocol.md)
- [StreamProtocol](streamprotocol.md)
### Conforming Types
- [Coder](coder.md)
- [Framer](framer.md)
- [QUICDatagram](quicdatagram.md)
- [QUICStream](quicstream.md)
- [TCP](tcp.md)
- [TLS](tls.md)
- [TLV](tlv.md)
- [UDP](udp.md)
- [WebSocket](websocket.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/onetooneprotocol)*