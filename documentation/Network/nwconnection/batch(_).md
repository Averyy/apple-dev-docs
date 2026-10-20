# batch(_:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Defines a block in which calls to send and receive are processed as a batch to improve performance.

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
final func batch(_ block: () -> Void)
```

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
- [NWConnection.ContentContext](./contentcontext.md)
  An object that represents a message to send or receive, containing protocol metadata and send properties.
- [var maximumDatagramSize: Int](./maximumdatagramsize.md)
  The maximum size of a datagram message that can be sent on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/batch(_:))*