# setSubprotocols(_:)

**Framework**: Network  
**Kind**: method

Adds to the list of supported application protocols that will be presented to a WebSocket server during connection establishment.

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
func setSubprotocols(_ subprotocols: [String])
```

## See Also

- [func setAdditionalHeaders([(name: String, value: String)])](nwprotocolwebsocket/options/setadditionalheaders(_:).md)
  Sets additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [var skipHandshake: Bool](nwprotocolwebsocket/options/skiphandshake.md)
  A Boolean indicating whether the WebSocket protocol skips its handshake and begins framing data once the underlying connection is established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/setsubprotocols(_:))*