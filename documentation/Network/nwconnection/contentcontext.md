# NWConnection.ContentContext

**Framework**: Network  
**Kind**: class  
**Role**: Class

An object that represents a message to send or receive, containing protocol metadata and send properties.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class ContentContext
```

#### Overview

For sending, you should use [`defaultMessage`](./contentcontext/defaultmessage.md) unless there is a reason to override some values.

You can pass [`finalMessage`](./contentcontext/finalmessage.md) to mark the final message in a connection. Once this context is used for sending, and the send is marked as complete, no more data can be sent on the connection.

If you are using a protocol that expects message content, like WebSocket or a custom framer, create a custom context and set metadata using [`protocolMetadata`](./contentcontext/protocolmetadata.md).

## Topics

### Using Constant Send Contexts
- [static let defaultMessage: NWConnection.ContentContext](./contentcontext/defaultmessage.md)
  A static context representing a message with default properties.
- [static let finalMessage: NWConnection.ContentContext](./contentcontext/finalmessage.md)
  A static context that’s marked as the final message in a connection.
- [static let defaultStream: NWConnection.ContentContext](./contentcontext/defaultstream.md)
  A static context representing the total stream of bytes on a connection.
### Creating Custom Send Contexts
- [init(identifier: String, expiration: UInt64, priority: Double, isFinal: Bool, antecedent: NWConnection.ContentContext?, metadata: [NWProtocolMetadata]?)](./contentcontext/init%28identifier,expiration,priority,isfinal,antecedent,metadata%29.md)
  Initializes a custom message context.
- [let identifier: String](./contentcontext/identifier.md)
  The identifier of the message, used for debugging.
- [var protocolMetadata: [NWProtocolMetadata]](./contentcontext/protocolmetadata.md)
  An array of protocol metadata used to configure per-message or per-packet properties.
- [class NWProtocolMetadata](../nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let antecedent: NWConnection.ContentContext?](./contentcontext/antecedent.md)
  An optional message context that must be sent before the context you are sending.
- [let expirationMilliseconds: UInt64](./contentcontext/expirationmilliseconds.md)
  A number of milliseconds after which sending the data associated with this context must begin, otherwise the data is discarded.
- [let relativePriority: Double](./contentcontext/relativepriority.md)
  A relative value of priority used to reorder contexts when sending.
### Inspecting Receive Contexts
- [let isFinal: Bool](./contentcontext/isfinal.md)
  A Boolean indicating whether this context represents the final message being sent or received.
- [func protocolMetadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](./contentcontext/protocolmetadata%28definition%29.md)
  Retreives the metadata associated with a specific protocol.

## Relationships

### Inherited By
- [NWConnectionGroup.Message](../nwconnectiongroup/message.md)
### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending and Receiving Data
- [func send(content: Data?, contentContext: NWConnection.ContentContext, isComplete: Bool, completion: NWConnection.SendCompletion)](./send%28content,contentcontext,iscomplete,completion%29-5ecuz.md)
  Sends data on a connection.
- [func send<Content>(content: Content?, contentContext: NWConnection.ContentContext, isComplete: Bool, completion: NWConnection.SendCompletion)](./send%28content,contentcontext,iscomplete,completion%29-3mfmt.md)
  Sends data on a connection using a custom Data type.
- [NWConnection.SendCompletion](./sendcompletion.md)
  A completion handler that indicates when the connection has finished processing sent content.
- [func receive(minimumIncompleteLength: Int, maximumLength: Int, completion: (Data?, NWConnection.ContentContext?, Bool, NWError?) -> Void)](./receive%28minimumincompletelength,maximumlength,completion%29.md)
  Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [func receiveMessage(completion: (Data?, NWConnection.ContentContext?, Bool, NWError?) -> Void)](./receivemessage%28completion%29.md)
  Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [func batch(() -> Void)](./batch%28_%29.md)
  Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [var maximumDatagramSize: Int](./maximumdatagramsize.md)
  The maximum size of a datagram message that can be sent on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/contentcontext)*