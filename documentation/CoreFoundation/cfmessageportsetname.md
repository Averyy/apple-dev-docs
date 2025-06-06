# CFMessagePortSetName(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the name of a local CFMessagePort object.

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
func CFMessagePortSetName(_ ms: CFMessagePort!, _ newName: CFString!) -> Bool
```

#### Return Value

`true` if the name change succeeds, otherwise `false`.

#### Discussion

Other threads and processes can connect to a named message port with [`CFMessagePortCreateRemote(_:_:)`](cfmessageportcreateremote(_:_:).md).

## Parameters

- `ms`: The local message port to examine.
- `newName`: The new name for  .

## See Also

- [func CFMessagePortCreateRunLoopSource(CFAllocator!, CFMessagePort!, CFIndex) -> CFRunLoopSource!](cfmessageportcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFMessagePort object.
- [func CFMessagePortSetInvalidationCallBack(CFMessagePort!, CFMessagePortInvalidationCallBack!)](cfmessageportsetinvalidationcallback(_:_:).md)
  Sets the callback function invoked when a CFMessagePort object is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportsetname(_:_:))*