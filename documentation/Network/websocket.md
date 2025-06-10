# WebSocket

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
struct WebSocket
```

## Topics

### Initializers
- [init()](websocket/init.md)
- [init<BelowProtocol>(() -> BelowProtocol)](websocket/init(_:)-5q53h.md)
- [init<BelowProtocol>(() -> BelowProtocol)](websocket/init(_:)-7xsae.md)
### Instance Properties
- [let belowProtocol: any NetworkProtocolOptions](websocket/belowprotocol.md)
### Instance Methods
- [func additionalHeaders([(name: String, value: String)]) -> WebSocket](websocket/additionalheaders(_:).md)
- [func autoReplyPing(Bool) -> WebSocket](websocket/autoreplyping(_:).md)
- [func maximumMessageSize(Int) -> WebSocket](websocket/maximummessagesize(_:).md)
- [func skipHandshake(Bool) -> WebSocket](websocket/skiphandshake(_:).md)
- [func subprotocols([String]) -> WebSocket](websocket/subprotocols(_:).md)

## Relationships

### Conforms To
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket)*