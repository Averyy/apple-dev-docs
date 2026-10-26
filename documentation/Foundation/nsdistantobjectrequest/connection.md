# connection

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the `NSConnection` object involved in the request.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (retain, readonly) NSConnection * connection;
```

#### Return Value

The `NSConnection` object involved in the request.

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Getting Information About a Request
- [conversation](./conversation.md)
  Returns the token object representing the conversation in which the receiver was created.
- [invocation](./invocation.md)
  Returns the `NSInvocation` object for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/connection)*