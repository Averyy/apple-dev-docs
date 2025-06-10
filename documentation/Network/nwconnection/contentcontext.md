# NWConnection.ContentContext

**Framework**: Network  
**Kind**: class

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

For sending, you should use [`defaultMessage`](nwconnection/contentcontext/defaultmessage.md) unless there is a reason to override some values.

You can pass [`finalMessage`](nwconnection/contentcontext/finalmessage.md) to mark the final message in a connection. Once this context is used for sending, and the send is marked as complete, no more data can be sent on the connection.

If you are using a protocol that expects message content, like WebSocket or a custom framer, create a custom context and set metadata using [`protocolMetadata`](nwconnection/contentcontext/protocolmetadata.md).

## Topics

### Using Constant Send Contexts
- [static let defaultMessage: NWConnection.ContentContext](nwconnection/contentcontext/defaultmessage.md)
  A static context representing a message with default properties.
- [static let finalMessage: NWConnection.ContentContext](nwconnection/contentcontext/finalmessage.md)
  A static context that’s marked as the final message in a connection.
- [static let defaultStream: NWConnection.ContentContext](nwconnection/contentcontext/defaultstream.md)
  A static context representing the total stream of bytes on a connection.
### Creating Custom Send Contexts
- [init(identifier: String, expiration: UInt64, priority: Double, isFinal: Bool, antecedent: NWConnection.ContentContext?, metadata: [NWProtocolMetadata]?)](nwconnection/contentcontext/init(identifier:expiration:priority:isfinal:antecedent:metadata:).md)
  Initializes a custom message context.
- [let identifier: String](nwconnection/contentcontext/identifier.md)
  The identifier of the message, used for debugging.
- [var protocolMetadata: [NWProtocolMetadata]](nwconnection/contentcontext/protocolmetadata.md)
  An array of protocol metadata used to configure per-message or per-packet properties.
- [class NWProtocolMetadata](nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let antecedent: NWConnection.ContentContext?](nwconnection/contentcontext/antecedent.md)
  An optional message context that must be sent before the context you are sending.
- [let expirationMilliseconds: UInt64](nwconnection/contentcontext/expirationmilliseconds.md)
  A number of milliseconds after which sending the data associated with this context must begin, otherwise the data is discarded.
- [let relativePriority: Double](nwconnection/contentcontext/relativepriority.md)
  A relative value of priority used to reorder contexts when sending.
### Inspecting Receive Contexts
- [let isFinal: Bool](nwconnection/contentcontext/isfinal.md)
  A Boolean indicating whether this context represents the final message being sent or received.
- [func protocolMetadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](nwconnection/contentcontext/protocolmetadata(definition:).md)
  Retreives the metadata associated with a specific protocol.

## Relationships

### Inherited By
- [NWConnectionGroup.Message](nwconnectiongroup/message.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func send(content: Data?, contentContext: NWConnection.ContentContext, isComplete: Bool, completion: NWConnection.SendCompletion)](nwconnection/send(content:contentcontext:iscomplete:completion:)-5ecuz.md)
  Sends data on a connection.
- [func send<Content>(content: Content?, contentContext: NWConnection.ContentContext, isComplete: Bool, completion: NWConnection.SendCompletion)](nwconnection/send(content:contentcontext:iscomplete:completion:)-3mfmt.md)
  Sends data on a connection using a custom Data type.
- [NWConnection.SendCompletion](nwconnection/sendcompletion.md)
  A completion handler that indicates when the connection has finished processing sent content.
- [func receive(minimumIncompleteLength: Int, maximumLength: Int, completion: (Data?, NWConnection.ContentContext?, Bool, NWError?) -> Void)](nwconnection/receive(minimumincompletelength:maximumlength:completion:).md)
  Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [func receiveMessage(completion: (Data?, NWConnection.ContentContext?, Bool, NWError?) -> Void)](nwconnection/receivemessage(completion:).md)
  Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [func batch(() -> Void)](nwconnection/batch(_:).md)
  Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [var maximumDatagramSize: Int](nwconnection/maximumdatagramsize.md)
  The maximum size of a datagram message that can be sent on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/contentcontext)*