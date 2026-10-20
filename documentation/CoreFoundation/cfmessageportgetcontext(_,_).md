# CFMessagePortGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the context information for a CFMessagePort object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFMessagePortGetContext(_ ms: CFMessagePort!, _ context: UnsafeMutablePointer<CFMessagePortContext>!)
```

```c
extern void CFMessagePortGetContext(CFMessagePortRef ms, CFMessagePortContext *context);
```

#### Discussion

The context version number for message ports is currently `0`. Before calling this function, you need to initialize the `version` member of `context` to `0`.

## Parameters

- `ms`: The message port to examine.
- `context`: A pointer to the structure into which the context information for `ms` is to be copied. The information being returned is usually the same information you passed to [`CFMessagePortCreateLocal(_:_:_:_:_:)`](./cfmessageportcreatelocal%28_,_,_,_,_%29.md) when creating `ms`. However, if [`CFMessagePortCreateLocal(_:_:_:_:_:)`](./cfmessageportcreatelocal%28_,_,_,_,_%29.md) returned a cached object instead of creating a new object, `context` is filled with information from the original message port instead of the information you passed to the function.

## See Also

### Examining a Message Port
- [func CFMessagePortGetInvalidationCallBack(CFMessagePort!) -> CFMessagePortInvalidationCallBack!](./cfmessageportgetinvalidationcallback%28_%29.md)
  Returns the invalidation callback function for a CFMessagePort object.
- [func CFMessagePortGetName(CFMessagePort!) -> CFString!](./cfmessageportgetname%28_%29.md)
  Returns the name with which a CFMessagePort object is registered.
- [func CFMessagePortIsRemote(CFMessagePort!) -> Bool](./cfmessageportisremote%28_%29.md)
  Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [func CFMessagePortIsValid(CFMessagePort!) -> Bool](./cfmessageportisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportgetcontext(_:_:))*