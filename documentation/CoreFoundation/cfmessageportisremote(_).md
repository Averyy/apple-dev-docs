# CFMessagePortIsRemote(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.

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
func CFMessagePortIsRemote(_ ms: CFMessagePort!) -> Bool
```

```c
extern Boolean CFMessagePortIsRemote(CFMessagePortRef ms);
```

## Return Value

`true` if `ms` is a remote port, otherwise `false`.

## Parameters

- `ms`: The message port to examine.

## See Also

### Examining a Message Port
- [func CFMessagePortGetContext(CFMessagePort!, UnsafeMutablePointer<CFMessagePortContext>!)](./cfmessageportgetcontext%28_,_%29.md)
  Returns the context information for a CFMessagePort object.
- [func CFMessagePortGetInvalidationCallBack(CFMessagePort!) -> CFMessagePortInvalidationCallBack!](./cfmessageportgetinvalidationcallback%28_%29.md)
  Returns the invalidation callback function for a CFMessagePort object.
- [func CFMessagePortGetName(CFMessagePort!) -> CFString!](./cfmessageportgetname%28_%29.md)
  Returns the name with which a CFMessagePort object is registered.
- [func CFMessagePortIsValid(CFMessagePort!) -> Bool](./cfmessageportisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportisremote(_:))*