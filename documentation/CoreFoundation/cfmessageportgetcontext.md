# CFMessagePortGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the context information for a CFMessagePort object.

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
func CFMessagePortGetContext(_ ms: CFMessagePort!, _ context: UnsafeMutablePointer<CFMessagePortContext>!)
```

#### Discussion

The context version number for message ports is currently `0`. Before calling this function, you need to initialize the `version` member of `context` to `0`.

## Parameters

- `ms`: The message port to examine.
- `context`: A pointer to the structure into which the context information for   is to be copied. The information being returned is usually the same information you passed to   when creating  . However, if   returned a cached object instead of creating a new object,   is filled with information from the original message port instead of the information you passed to the function.

## See Also

- [func CFMessagePortGetInvalidationCallBack(CFMessagePort!) -> CFMessagePortInvalidationCallBack!](cfmessageportgetinvalidationcallback(_:).md)
  Returns the invalidation callback function for a CFMessagePort object.
- [func CFMessagePortGetName(CFMessagePort!) -> CFString!](cfmessageportgetname(_:).md)
  Returns the name with which a CFMessagePort object is registered.
- [func CFMessagePortIsRemote(CFMessagePort!) -> Bool](cfmessageportisremote(_:).md)
  Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [func CFMessagePortIsValid(CFMessagePort!) -> Bool](cfmessageportisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportgetcontext(_:_:))*