# CFMessagePortGetInvalidationCallBack(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the invalidation callback function for a CFMessagePort object.

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
func CFMessagePortGetInvalidationCallBack(_ ms: CFMessagePort!) -> CFMessagePortInvalidationCallBack!
```

#### Return Value

The callback function invoked when `ms` is invalidated. `NULL` if no callback has been set with [`CFMessagePortSetInvalidationCallBack(_:_:)`](cfmessageportsetinvalidationcallback(_:_:).md).

## Parameters

- `ms`: The message port to examine.

## See Also

- [func CFMessagePortGetContext(CFMessagePort!, UnsafeMutablePointer<CFMessagePortContext>!)](cfmessageportgetcontext(_:_:).md)
  Returns the context information for a CFMessagePort object.
- [func CFMessagePortGetName(CFMessagePort!) -> CFString!](cfmessageportgetname(_:).md)
  Returns the name with which a CFMessagePort object is registered.
- [func CFMessagePortIsRemote(CFMessagePort!) -> Bool](cfmessageportisremote(_:).md)
  Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [func CFMessagePortIsValid(CFMessagePort!) -> Bool](cfmessageportisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportgetinvalidationcallback(_:))*