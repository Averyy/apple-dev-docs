# CFMachPortSetInvalidationCallBack(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the callback function invoked when a CFMachPort object is invalidated.

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
func CFMachPortSetInvalidationCallBack(_ port: CFMachPort!, _ callout: CFMachPortInvalidationCallBack!)
```

#### Discussion

If `port` is already invalid, `callout` is invoked immediately.

## Parameters

- `port`: The CFMachPort object to modify.
- `callout`: The callback function to invoke when   is invalidated. Pass   to remove a callback.

## See Also

- [func CFMachPortInvalidate(CFMachPort!)](cfmachportinvalidate(_:).md)
  Invalidates a CFMachPort object, stopping it from receiving any more messages.
- [func CFMachPortCreateRunLoopSource(CFAllocator!, CFMachPort!, CFIndex) -> CFRunLoopSource!](cfmachportcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFMachPort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportsetinvalidationcallback(_:_:))*