# CFMachPortCreateRunLoopSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFRunLoopSource object for a CFMachPort object.

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
func CFMachPortCreateRunLoopSource(_ allocator: CFAllocator!, _ port: CFMachPort!, _ order: CFIndex) -> CFRunLoopSource!
```

#### Return Value

The new CFRunLoopSource object for `port`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The run loop source is not automatically added to a run loop. To add the source to a run loop, use [`CFRunLoopAddSource(_:_:_:)`](cfrunloopaddsource(_:_:_:).md).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `port`: The Mach port for which to create a CFRunLoopSource object.
- `order`: A priority index indicating the order in which run loop sources are processed.   is currently ignored by CFMachPort run loop sources. Pass   for this value.

## See Also

- [func CFMachPortInvalidate(CFMachPort!)](cfmachportinvalidate(_:).md)
  Invalidates a CFMachPort object, stopping it from receiving any more messages.
- [func CFMachPortSetInvalidationCallBack(CFMachPort!, CFMachPortInvalidationCallBack!)](cfmachportsetinvalidationcallback(_:_:).md)
  Sets the callback function invoked when a CFMachPort object is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportcreaterunloopsource(_:_:_:))*