# NWConnectionGroup.Message

**Framework**: Network  
**Kind**: class

An object that represents a message that you send or receive within a group, and that contains protocol metadata and send properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class Message
```

## Topics

### Inspecting Received Messages
- [var remoteEndpoint: NWEndpoint?](nwconnectiongroup/message/remoteendpoint.md)
  The endpoint that originates the message you receive.
- [var localEndpoint: NWEndpoint?](nwconnectiongroup/message/localendpoint.md)
  The local address and port you use to receive the message.
- [var path: NWPath?](nwconnectiongroup/message/path.md)
  The network path on which you receive the message.
### Replying to Received Messages
- [func reply(content: Data?, message: NWConnectionGroup.Message)](nwconnectiongroup/message/reply(content:message:).md)
  Sends a reply to the specific endpoint that originates a group message you receive.
- [func extractConnection() -> NWConnection?](nwconnectiongroup/message/extractconnection.md)
  Converts a message you receive from an endpoint into a connection object that you use for long-term communication with that endpoint.
### Sending Messages
- [static let `default`: NWConnectionGroup.Message](nwconnectiongroup/message/default.md)
  A static object you use to send a message with default properties.
- [init(identifier: String, expiration: UInt64, priority: Double, isFinal: Bool, antecedent: NWConnection.ContentContext?, metadata: [NWProtocolMetadata]?)](nwconnectiongroup/message/init(identifier:expiration:priority:isfinal:antecedent:metadata:).md)
  Initializes a custom message context you use to send data.
### Initializers
- [init(nw: nw_content_context_t)](nwconnectiongroup/message/init(nw:).md)
### Instance Methods
- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](nwconnectiongroup/message/metadata(definition:).md)

## Relationships

### Inherits From
- [NWConnection.ContentContext](nwconnection/contentcontext.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setReceiveHandler(maximumMessageSize: Int, rejectOversizedMessages: Bool, handler: ((NWConnectionGroup.Message, Data?, Bool) -> Void)?)](nwconnectiongroup/setreceivehandler(maximummessagesize:rejectoversizedmessages:handler:).md)
  Sets a handler that receives inbound messages from members of the group.
- [func send(content: Data?, to: NWEndpoint?, message: NWConnectionGroup.Message, completion: (NWError?) -> Void)](nwconnectiongroup/send(content:to:message:completion:).md)
  Sends data to the entire group, or to a specific member of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/message)*