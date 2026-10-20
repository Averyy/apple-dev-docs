# NWProtocolWebSocket.Options

**Framework**: Network  
**Kind**: class  
**Role**: Class

A container of options for configuring how WebSocket is used on a connection.

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
class Options
```

## Topics

### Configuring WebSocket Options
- [init(NWProtocolWebSocket.Version)](./options/init%28_%29.md)
  Initializes a default set of WebSocket connection options.
- [NWProtocolWebSocket.Version](./version.md)
  Supported versions of the WebSocket protocol.
- [var autoReplyPing: Bool](./options/autoreplyping.md)
  A Boolean indicating whether the connection automatically replies to Ping messages instead of delivering them to you.
- [var maximumMessageSize: Int](./options/maximummessagesize.md)
  The maximum allowed message size, in bytes, to be received by the WebSocket connection.
### Configuring Client Handshakes
- [func setAdditionalHeaders([(name: String, value: String)])](./options/setadditionalheaders%28_%29.md)
  Sets additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [func setSubprotocols([String])](./options/setsubprotocols%28_%29.md)
  Adds to the list of supported application protocols that will be presented to a WebSocket server during connection establishment.
- [var skipHandshake: Bool](./options/skiphandshake.md)
  A Boolean indicating whether the WebSocket protocol skips its handshake and begins framing data once the underlying connection is established.
### Handling Server Handshakes
- [func setClientRequestHandler(DispatchQueue, handler: ([String], [(name: String, value: String)]) -> NWProtocolWebSocket.Response)](./options/setclientrequesthandler%28_,handler%29.md)
  Sets a handler to react to as a server to inbound WebSocket client handshakes.
- [NWProtocolWebSocket.Response](./response.md)
  A WebSocket handshake reponse sent from a server to a client.

## Relationships

### Inherits From
- [NWProtocolOptions](../nwprotocoloptions.md)
### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating WebSocket Connections
- [static let definition: NWProtocolDefinition](./definition.md)
  The system definition of the WebSocket protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/options)*