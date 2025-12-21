# additionalHeaders(_:)

**Framework**: Network  
**Kind**: method

Set additional HTTP header fields to be sent by the client during the WebSocket handshake.

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
func additionalHeaders(_ headers: [(name: String, value: String)]) -> WebSocket
```

#### Discussion

This can be used for custom protocols and cookies. Multiple headers of the same name are not allowed, and the header will replaced by the most recently set value.

> **Note**: This function will only take effect on WebSocket clients.

## Parameters

- `headers`: An array of HTTP header field names and values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket/additionalheaders(_:))*