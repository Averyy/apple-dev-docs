# CFMessagePortCreateRunLoopSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a CFRunLoopSource object for a CFMessagePort object.

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
func CFMessagePortCreateRunLoopSource(_ allocator: CFAllocator!, _ local: CFMessagePort!, _ order: CFIndex) -> CFRunLoopSource!
```

```c
extern CFRunLoopSourceRefCFMessagePortCreateRunLoopSource(CFAllocatorRef allocator, CFMessagePortRef local, CFIndex order);
```

## Return Value

The new CFRunLoopSource object for `ms`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The run loop source is not automatically added to a run loop. To add the source to a run loop, use [`CFRunLoopAddSource(_:_:_:)`](./cfrunloopaddsource%28_,_,_%29.md).

### Special Considerations

This method is not available on iOS 7 and later—it will return `NULL` and log a sandbox violation in `syslog`. See [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091) for possible replacement technologies.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `local`: The message port for which to create a run loop source.
- `order`: A priority index indicating the order in which run loop sources are processed. `order` is currently ignored by CFMessagePort object run loop sources. Pass `0` for this value.

## See Also

### Configuring a CFMessagePort Object
- [func CFMessagePortSetInvalidationCallBack(CFMessagePort!, CFMessagePortInvalidationCallBack!)](./cfmessageportsetinvalidationcallback%28_,_%29.md)
  Sets the callback function invoked when a CFMessagePort object is invalidated.
- [func CFMessagePortSetName(CFMessagePort!, CFString!) -> Bool](./cfmessageportsetname%28_,_%29.md)
  Sets the name of a local CFMessagePort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportcreaterunloopsource(_:_:_:))*