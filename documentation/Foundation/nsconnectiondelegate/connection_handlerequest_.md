# connection:handleRequest:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (BOOL) connection:(NSConnection *) connection handleRequest:(NSDistantObjectRequest *) doreq;
```

## Return Value

[`true`](../../Swift/true.md) if the request was handled by the delegate, [`false`](../../Swift/false.md) if the request should proceed as if the delegate did not intercept it.

## Parameters

- `connection`: The connection object for which the receiver is the delegate.
- `doreq`: The distant object request.

## See Also

### Responding to a Connection
- [- connection:shouldMakeNewConnection:](./connection_shouldmakenewconnection_.md)
  Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created.
- [- createConversationForConnection:](./createconversationforconnection_.md)
  Returns an arbitrary object identifying a new conversation being created for the connection in the current thread.
- [- makeNewConnection:sender:](./makenewconnection_sender_.md)
  Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/connection:handlerequest:)*