# CFMessagePortGetName(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the name with which a CFMessagePort object is registered.

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
func CFMessagePortGetName(_ ms: CFMessagePort!) -> CFString!
```

```c
extern CFStringRefCFMessagePortGetName(CFMessagePortRef ms);
```

## Return Value

The registered name of `ms`, `NULL` if unnamed. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `ms`: The message port to examine.

## See Also

### Examining a Message Port
- [func CFMessagePortGetContext(CFMessagePort!, UnsafeMutablePointer<CFMessagePortContext>!)](./cfmessageportgetcontext%28_,_%29.md)
  Returns the context information for a CFMessagePort object.
- [func CFMessagePortGetInvalidationCallBack(CFMessagePort!) -> CFMessagePortInvalidationCallBack!](./cfmessageportgetinvalidationcallback%28_%29.md)
  Returns the invalidation callback function for a CFMessagePort object.
- [func CFMessagePortIsRemote(CFMessagePort!) -> Bool](./cfmessageportisremote%28_%29.md)
  Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [func CFMessagePortIsValid(CFMessagePort!) -> Bool](./cfmessageportisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportgetname(_:))*