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

- `remote`: The message port to which `data` should be sent.
- `msgid`: An arbitrary integer value that you can send with the message.
- `data`: The data to send to `remote`.
- `sendTimeout`: The time to wait for `data` to be sent.
- `rcvTimeout`: The time to wait for a reply to be returned.
- `replyMode`: The run loop mode in which the function should wait for a reply. If the message is a `oneway` (so no response is expected), then `replyMode` should be `NULL`. If `replyMode` is non-`NULL`, the function runs the run loop waiting for a reply, in that mode. `replyMode` can be any string name of a run loop mode, but it should be one with input sources installed. You should use the `kCFRunLoopDefaultMode` constant unless you have a specific reason to use a different mode.
- `returnData`: Upon return, contains a CFData object containing the reply data. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

- [func CFMessagePortInvalidate(CFMessagePort!)](cfmessageportinvalidate(_:).md)
  Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.
- [func CFMessagePortSetDispatchQueue(CFMessagePort!, dispatch_queue_t!)](cfmessageportsetdispatchqueue(_:_:).md)
  Schedules callbacks for the specified message port on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportsendrequest(_:_:_:_:_:_:_:))*