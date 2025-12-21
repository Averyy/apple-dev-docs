# init(_:)

**Framework**: Network  
**Kind**: init

Create an instance of the WebSocket protocol.

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
init<BelowProtocol>(@ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : StreamProtocol
```

## Parameters

- `builder`: The protocol stack below WebSocket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket/init(_:)-7xsae)*