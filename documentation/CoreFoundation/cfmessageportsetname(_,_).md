# CFMessagePortSetName(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the name of a local CFMessagePort object.

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
func CFMessagePortSetName(_ ms: CFMessagePort!, _ newName: CFString!) -> Bool
```

```c
extern Boolean CFMessagePortSetName(CFMessagePortRef ms, CFStringRef newName);
```

#### Return Value

`true` if the name change succeeds, otherwise `false`.

#### Discussion

Other threads and processes can connect to a named message port with [`CFMessagePortCreateRemote(_:_:)`](./cfmessageportcreateremote%28_,_%29.md).

## Parameters

- `ms`: The local message port to examine.
- `newName`: The new name for `ms`.

## See Also

### Configuring a CFMessagePort Object
- [func CFMessagePortCreateRunLoopSource(CFAllocator!, CFMessagePort!, CFIndex) -> CFRunLoopSource!](./cfmessageportcreaterunloopsource%28_,_,_%29.md)
  Creates a CFRunLoopSource object for a CFMessagePort object.
- [func CFMessagePortSetInvalidationCallBack(CFMessagePort!, CFMessagePortInvalidationCallBack!)](./cfmessageportsetinvalidationcallback%28_,_%29.md)
  Sets the callback function invoked when a CFMessagePort object is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportsetname(_:_:))*