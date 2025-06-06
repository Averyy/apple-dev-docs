# send(content:contentContext:isComplete:completion:)

**Framework**: Network  
**Kind**: method

Sends data on a connection.

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
@preconcurrency
final func send(content: Data?, contentContext: NWConnection.ContentContext = .defaultMessage, isComplete: Bool = true, completion: NWConnection.SendCompletion)
```

## Parameters

- `content`: The data to send on the connection. May be nil if this send marks its context as complete, such as by sending   as the context and marking the send complete to send a write-close.
- `contentContext`: The context associated with the content, which represents a logical message to be sent on the connection. All content sent within a single context will be sent as an in-order unit, up until the point that the context is marked complete. Once a context is marked complete, it may be re-used as a new logical message. Protocols like TCP that cannot send multiple independent messages at once (serial bytestreams) will only start processing a new context once the prior context has been marked complete. Defaults to  .
- `isComplete`: When sending using streaming protocols like TCP, this flag can be used to mark the end of a single message on the stream, of which there may be many. However, it can also indicate that the connection should send a “write close” (a TCP FIN) if the sending context is the final context on the connection. Specifically, to send a “write close”, pass   or   for the context (or create a custom context and set  ), and mark the send as complete.
- `completion`: A completion handler ( ) to notify the caller when content has been processed by the connection, or a marker that this data is idempotent ( ) and may be sent multiple times as fast open data if   is set.

## See Also

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
- [NWConnection.ContentContext](nwconnection/contentcontext.md)
  An object that represents a message to send or receive, containing protocol metadata and send properties.
- [var maximumDatagramSize: Int](nwconnection/maximumdatagramsize.md)
  The maximum size of a datagram message that can be sent on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/send(content:contentcontext:iscomplete:completion:)-5ecuz)*