# CFMessagePortCreateRemote(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a CFMessagePort object connected to a remote port.

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
func CFMessagePortCreateRemote(_ allocator: CFAllocator!, _ name: CFString!) -> CFMessagePort!
```

#### Return Value

The new CFMessagePort object, or `NULL` on failure. If a message port has already been created for the remote port, the pre-existing object is returned. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This method is not available on iOS 7 and later—it will return `NULL` and log a sandbox violation in `syslog`. See [`Concurrency Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091) for possible replacement technologies.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `name`: The name of the remote message port to which to connect.

## See Also

- [func CFMessagePortCreateLocal(CFAllocator!, CFString!, CFMessagePortCallBack!, UnsafeMutablePointer<CFMessagePortContext>!, UnsafeMutablePointer<DarwinBoolean>!) -> CFMessagePort!](cfmessageportcreatelocal(_:_:_:_:_:).md)
  Returns a local CFMessagePort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportcreateremote(_:_:))*