# CFMessagePortSetInvalidationCallBack(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the callback function invoked when a CFMessagePort object is invalidated.

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
func CFMessagePortSetInvalidationCallBack(_ ms: CFMessagePort!, _ callout: CFMessagePortInvalidationCallBack!)
```

```c
extern void CFMessagePortSetInvalidationCallBack(CFMessagePortRef ms, CFMessagePortInvalidationCallBack callout);
```

#### Discussion

If `ms` is already invalid, `callout` is invoked immediately.

## Parameters

- `ms`: The message port to examine.
- `callout`: The callback function to invoke when `ms` is invalidated. Pass `NULL` to remove a callback.

## See Also

### Configuring a CFMessagePort Object
- [func CFMessagePortCreateRunLoopSource(CFAllocator!, CFMessagePort!, CFIndex) -> CFRunLoopSource!](./cfmessageportcreaterunloopsource%28_,_,_%29.md)
  Creates a CFRunLoopSource object for a CFMessagePort object.
- [func CFMessagePortSetName(CFMessagePort!, CFString!) -> Bool](./cfmessageportsetname%28_,_%29.md)
  Sets the name of a local CFMessagePort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportsetinvalidationcallback(_:_:))*