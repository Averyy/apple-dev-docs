# currentConversation

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a token object representing any conversation in progress in the current thread.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
+ (id) currentConversation;
```

## Return Value

A token object representing any conversation in progress in the current thread, or `nil` if there is no conversation in progress.

## See Also

### Related Documentation
- [- createConversationForConnection:](../nsconnectiondelegate/createconversationforconnection_.md)
  Returns an arbitrary object identifying a new conversation being created for the connection in the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/currentconversation)*