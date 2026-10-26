# invocation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the `NSInvocation` object for the request.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (retain, readonly) NSInvocation * invocation;
```

#### Return Value

The `NSInvocation` object for the request.

## See Also

### Getting Information About a Request
- [connection](./connection.md)
  Returns the `NSConnection` object involved in the request.
- [conversation](./conversation.md)
  Returns the token object representing the conversation in which the receiver was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/invocation)*