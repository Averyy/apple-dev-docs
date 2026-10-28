# conversation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the token object representing the conversation in which the receiver was created.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (retain, readonly) id conversation;
```

## Return Value

The token object representing the conversation in which the receiver was created.

## Discussion

If both ends of the distributed objects connection has [`independentConversationQueueing`](../nsconnection/independentconversationqueueing.md) set to [`false`](../../Swift/false.md) (the default), the conversation object is always `nil`. Otherwise, it is either a proxy (or a copy) of the object created by the sender of the message or a locally created object, depending which end of the connection has independent queueing on.

## See Also

### Getting Information About a Request
- [connection](./connection.md)
  Returns the `NSConnection` object involved in the request.
- [invocation](./invocation.md)
  Returns the `NSInvocation` object for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/conversation)*