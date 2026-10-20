# init(_:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a default set of WebSocket connection options.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(_ version: NWProtocolWebSocket.Version = .version13)
```

## See Also

### Configuring WebSocket Options
- [NWProtocolWebSocket.Version](../version.md)
  Supported versions of the WebSocket protocol.
- [var autoReplyPing: Bool](./autoreplyping.md)
  A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.
- [var maximumMessageSize: Int](./maximummessagesize.md)
  The maximum allowed message size, in bytes, to be received by the WebSocket connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/init(_:))*