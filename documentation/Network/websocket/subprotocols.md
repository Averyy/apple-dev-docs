# subprotocols(_:)

**Framework**: Network  
**Kind**: method

Set the list of supported application protocols that will be presented to a WebSocket server during connection establishment.

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
func subprotocols(_ subprotocols: [String]) -> WebSocket
```

#### Discussion

> **Note**: This function will only take effect on WebSocket clients.

## Parameters

- `subprotocols`: An array of subprotocol strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket/subprotocols(_:))*