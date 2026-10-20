# maximumDatagramSize

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

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
- [NWConnection.ContentContext](./contentcontext.md)
  An object that represents a message to send or receive, containing protocol metadata and send properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/maximumdatagramsize)*