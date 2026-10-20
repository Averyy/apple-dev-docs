# CFMachPortSetInvalidationCallBack(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the callback function invoked when a CFMachPort object is invalidated.

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
func CFMachPortSetInvalidationCallBack(_ port: CFMachPort!, _ callout: CFMachPortInvalidationCallBack!)
```

```c
extern void CFMachPortSetInvalidationCallBack(CFMachPortRef port, CFMachPortInvalidationCallBack callout);
```

#### Discussion

If `port` is already invalid, `callout` is invoked immediately.

## Parameters

- `port`: The CFMachPort object to modify.
- `callout`: The callback function to invoke when `port` is invalidated. Pass `NULL` to remove a callback.

## See Also

### Configuring a CFMachPort Object
- [func CFMachPortInvalidate(CFMachPort!)](./cfmachportinvalidate%28_%29.md)
  Invalidates a CFMachPort object, stopping it from receiving any more messages.
- [func CFMachPortCreateRunLoopSource(CFAllocator!, CFMachPort!, CFIndex) -> CFRunLoopSource!](./cfmachportcreaterunloopsource%28_,_,_%29.md)
  Creates a CFRunLoopSource object for a CFMachPort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportsetinvalidationcallback(_:_:))*