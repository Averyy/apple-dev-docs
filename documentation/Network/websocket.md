# WebSocket

**Framework**: Network  
**Kind**: struct

The system definition of the WebSocket protocol.

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
struct WebSocket
```

#### Overview

Can be used to add WebSocket to a protocol stack and configure its options.

## Topics

### Initializers
- [init<BelowProtocol>(() -> BelowProtocol)](websocket/init(_:)-5q53h.md)
  Create an instance of the WebSocket protocol.
- [init<BelowProtocol>(() -> BelowProtocol)](websocket/init(_:)-7xsae.md)
  Create an instance of the WebSocket protocol.
### Instance Methods
- [func additionalHeaders([(name: String, value: String)]) -> WebSocket](websocket/additionalheaders(_:).md)
  Set additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [func autoReplyPing(Bool) -> WebSocket](websocket/autoreplyping(_:).md)
  Configure the WebSocket protocol to automatically reply to pings.
- [func maximumMessageSize(Int) -> WebSocket](websocket/maximummessagesize(_:).md)
  Set the maximum allowed message size to be received by the WebSocket connection.
- [func skipHandshake(Bool) -> WebSocket](websocket/skiphandshake(_:).md)
  Configure the WebSocket protocol to skip the opening handshake and begin framing data as soon as the underlying connection is established.
- [func subprotocols([String]) -> WebSocket](websocket/subprotocols(_:).md)
  Set the list of supported application protocols that will be presented to a WebSocket server during connection establishment.

## Relationships

### Conforms To
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket)*