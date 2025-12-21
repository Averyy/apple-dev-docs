# MessageProtocol

**Framework**: Network  
**Kind**: protocol

Types that conform to MessageProtocol send and receive messages. The conforming type is responsible for specifying its message-specific metadata.

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
protocol MessageProtocol : OneToOneProtocol
```

## Topics

### Associated Types
- [associatedtype ContentType](messageprotocol/contenttype.md)
- [associatedtype LegacyMessage](messageprotocol/legacymessage.md)

## Relationships

### Inherits From
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)
### Inherited By
- [DatagramProtocol](datagramprotocol.md)
### Conforming Types
- [Coder](coder.md)
- [Framer](framer.md)
- [QUICDatagram](quicdatagram.md)
- [TLV](tlv.md)
- [UDP](udp.md)
- [WebSocket](websocket.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/messageprotocol)*