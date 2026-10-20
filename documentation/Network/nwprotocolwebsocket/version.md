# NWProtocolWebSocket.Version

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

Supported versions of the WebSocket protocol.

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
enum Version
```

## Topics

### Versions
- [NWProtocolWebSocket.Version.version13](./version/version13.md)
  Version 13 of the WebSocket protocol.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring WebSocket Options
- [init(NWProtocolWebSocket.Version)](./options/init%28_%29.md)
  Initializes a default set of WebSocket connection options.
- [var autoReplyPing: Bool](./options/autoreplyping.md)
  A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.
- [var maximumMessageSize: Int](./options/maximummessagesize.md)
  The maximum allowed message size, in bytes, to be received by the WebSocket connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/version)*