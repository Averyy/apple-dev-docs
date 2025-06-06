# maximumDatagramSize

**Framework**: Network  
**Kind**: property

The maximum size of a datagram message that can be sent on a connection.

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
final var maximumDatagramSize: Int { get }
```

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
- [NWConnection.ContentContext](nwconnection/contentcontext.md)
  An object that represents a message to send or receive, containing protocol metadata and send properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/maximumdatagramsize)*