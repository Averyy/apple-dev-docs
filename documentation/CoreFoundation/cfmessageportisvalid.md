# CFMessagePortIsValid(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.

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
func CFMessagePortIsValid(_ ms: CFMessagePort!) -> Bool
```

#### Return Value

`true` if `ms` can be used for communication, otherwise `false`.

## Parameters

- `ms`: The message port to examine.

## See Also

- [func CFMessagePortGetContext(CFMessagePort!, UnsafeMutablePointer<CFMessagePortContext>!)](cfmessageportgetcontext(_:_:).md)
  Returns the context information for a CFMessagePort object.
- [func CFMessagePortGetInvalidationCallBack(CFMessagePort!) -> CFMessagePortInvalidationCallBack!](cfmessageportgetinvalidationcallback(_:).md)
  Returns the invalidation callback function for a CFMessagePort object.
- [func CFMessagePortGetName(CFMessagePort!) -> CFString!](cfmessageportgetname(_:).md)
  Returns the name with which a CFMessagePort object is registered.
- [func CFMessagePortIsRemote(CFMessagePort!) -> Bool](cfmessageportisremote(_:).md)
  Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportisvalid(_:))*