# setAdditionalHeaders(_:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Sets additional HTTP header fields to be sent by the client during the WebSocket handshake.

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
func setAdditionalHeaders(_ headers: [(name: String, value: String)])
```

## See Also

### Configuring Client Handshakes
- [func setSubprotocols([String])](./setsubprotocols%28_%29.md)
  Adds to the list of supported application protocols that will be presented to a WebSocket server during connection establishment.
- [var skipHandshake: Bool](./skiphandshake.md)
  A Boolean indicating whether the WebSocket protocol skips its handshake and begins framing data once the underlying connection is established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/setadditionalheaders(_:))*