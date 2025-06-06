# CFMessagePortSendRequest(_:_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sends a message to a remote CFMessagePort object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFMessagePortSendRequest(_ remote: CFMessagePort!, _ msgid: Int32, _ data: CFData!, _ sendTimeout: CFTimeInterval, _ rcvTimeout: CFTimeInterval, _ replyMode: CFString!, _ returnData: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> Int32
```

#### Return Value

Error code indicating success or failure. See [`CFMessagePortSendRequest Error Codes`](1561514-cfmessageportsendrequest-error-c.md) for the possible return values.

## Parameters

- `remote`: The message port to which   should be sent.
- `msgid`: An arbitrary integer value that you can send with the message.
- `data`: The data to send to  .
- `sendTimeout`: The time to wait for   to be sent.
- `rcvTimeout`: The time to wait for a reply to be returned.
- `replyMode`: The run loop mode in which the function should wait for a reply. If the message is a   (so no response is expected), then   should be  . If   is non- , the function runs the run loop waiting for a reply, in that mode.   can be any string name of a run loop mode, but it should be one with input sources installed. You should use the   constant unless you have a specific reason to use a different mode.
- `returnData`: Upon return, contains a CFData object containing the reply data. Ownership follows the  .

## See Also

- [func CFMessagePortInvalidate(CFMessagePort!)](cfmessageportinvalidate(_:).md)
  Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.
- [func CFMessagePortSetDispatchQueue(CFMessagePort!, dispatch_queue_t!)](cfmessageportsetdispatchqueue(_:_:).md)
  Schedules callbacks for the specified message port on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportsendrequest(_:_:_:_:_:_:_:))*