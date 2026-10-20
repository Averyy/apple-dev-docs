# maximumMessageSize

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The maximum allowed message size, in bytes, to be received by the WebSocket connection.

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
var maximumMessageSize: Int { get set }
```

## See Also

### Configuring WebSocket Options
- [init(NWProtocolWebSocket.Version)](./init%28_%29.md)
  Initializes a default set of WebSocket connection options.
- [NWProtocolWebSocket.Version](../version.md)
  Supported versions of the WebSocket protocol.
- [var autoReplyPing: Bool](./autoreplyping.md)
  A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/maximummessagesize)*