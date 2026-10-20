# CFMessagePortIsValid(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.

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
func CFMessagePortIsValid(_ ms: CFMessagePort!) -> Bool
```

```c
extern Boolean CFMessagePortIsValid(CFMessagePortRef ms);
```

#### Return Value

`true` if `ms` can be used for communication, otherwise `false`.

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
- [func CFMessagePortIsRemote(CFMessagePort!) -> Bool](./cfmessageportisremote%28_%29.md)
  Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportisvalid(_:))*