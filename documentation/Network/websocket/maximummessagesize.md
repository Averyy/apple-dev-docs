# maximumMessageSize(_:)

**Framework**: Network  
**Kind**: method

Set the maximum allowed message size to be received by the WebSocket connection.

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
func maximumMessageSize(_ size: Int) -> WebSocket
```

#### Discussion

This does not limit the sending message size.

A maximum message size of 0 means there is no receive limit. The default maximum message size is 0.

## Parameters

- `size`: The maximum message size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket/maximummessagesize(_:))*