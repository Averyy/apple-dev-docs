# WebSocket

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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
- [init<BelowProtocol>(() -> BelowProtocol)](./websocket/init%28_%29-5q53h.md)
  Create an instance of the WebSocket protocol.
- [init<BelowProtocol>(() -> BelowProtocol)](./websocket/init%28_%29-7xsae.md)
  Create an instance of the WebSocket protocol.
### Instance Methods
- [func additionalHeaders([(name: String, value: String)]) -> WebSocket](./websocket/additionalheaders%28_%29.md)
  Set additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [func autoReplyPing(Bool) -> WebSocket](./websocket/autoreplyping%28_%29.md)
  Configure the WebSocket protocol to automatically reply to pings.
- [func maximumMessageSize(Int) -> WebSocket](./websocket/maximummessagesize%28_%29.md)
  Set the maximum allowed message size to be received by the WebSocket connection.
- [func skipHandshake(Bool) -> WebSocket](./websocket/skiphandshake%28_%29.md)
  Configure the WebSocket protocol to skip the opening handshake and begin framing data as soon as the underlying connection is established.
- [func subprotocols([String]) -> WebSocket](./websocket/subprotocols%28_%29.md)
  Set the list of supported application protocols that will be presented to a WebSocket server during connection establishment.

## Relationships

### Conforms To
- [MessageProtocol](./messageprotocol.md)
- [NetworkProtocolOptions](./networkprotocoloptions.md)
- [OneToOneProtocol](./onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket)*