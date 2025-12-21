# autoReplyPing(_:)

**Framework**: Network  
**Kind**: method

Configure the WebSocket protocol to automatically reply to pings.

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
func autoReplyPing(_ reply: Bool) -> WebSocket
```

## Parameters

- `reply`: If true, ping messages will   automatically be consumed by the connection instead of being   delivered to the . Defaults to false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket/autoreplyping(_:))*