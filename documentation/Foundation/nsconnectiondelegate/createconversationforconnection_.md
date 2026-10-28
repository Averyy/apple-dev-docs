# createConversationForConnection:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an arbitrary object identifying a new conversation being created for the connection in the current thread.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (id) createConversationForConnection:(NSConnection *) conn;
```

## Return Value

An arbitrary object identifying a new conversation being created for the connection in the current thread.

## Discussion

New conversations are created only if [`independentConversationQueueing`](../nsconnection/independentconversationqueueing.md) is [`true`](../../Swift/true.md) for `conn`. If you do not implement this method, `NSConnection` object creates an instance of `NSObject`.

## Parameters

- `conn`: The connection object for which the receiver is the delegate.

## See Also

### Related Documentation
- [+ currentConversation](../nsconnection/currentconversation.md)
  Returns a token object representing any conversation in progress in the current thread.
### Responding to a Connection
- [- connection:shouldMakeNewConnection:](./connection_shouldmakenewconnection_.md)
  Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created.
- [- connection:handleRequest:](./connection_handlerequest_.md)
  This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests.
- [- makeNewConnection:sender:](./makenewconnection_sender_.md)
  Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/createconversationforconnection:)*