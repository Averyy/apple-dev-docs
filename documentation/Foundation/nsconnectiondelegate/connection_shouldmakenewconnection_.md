# connection:shouldMakeNewConnection:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (BOOL) connection:(NSConnection *) ancestor shouldMakeNewConnection:(NSConnection *) conn;
```

#### Return Value

[`true`](../../Swift/true.md) if `ancestor` should allow `conn` to be created and set up, [`false`](../../Swift/false.md) if `ancestor` should refuse and immediately release `conn`.

#### Discussion

Use this method to limit the amount of `NSConnection` objects created in your application or to change the parameters of child `NSConnection` objects.

Use [`NSConnectionDidInitializeNotification`](../nsconnectiondidinitializenotification.md) instead of this delegate method if possible.

## Parameters

- `ancestor`: The connection object for which the receiver is the delegate.
- `conn`: The new connection.

## See Also

### Responding to a Connection
- [- connection:handleRequest:](./connection_handlerequest_.md)
  This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests.
- [- createConversationForConnection:](./createconversationforconnection_.md)
  Returns an arbitrary object identifying a new conversation being created for the connection in the current thread.
- [- makeNewConnection:sender:](./makenewconnection_sender_.md)
  Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/connection:shouldmakenewconnection:)*