# CFMessagePortCreateLocal(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a local CFMessagePort object.

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
func CFMessagePortCreateLocal(_ allocator: CFAllocator!, _ name: CFString!, _ callout: CFMessagePortCallBack!, _ context: UnsafeMutablePointer<CFMessagePortContext>!, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>!) -> CFMessagePort!
```

#### Return Value

The new CFMessagePort object, or `NULL` on failure. If a local port is already named `name`, the function returns that port instead of creating a new object; the `context` and `callout` parameters are ignored in this case. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This method is not available on iOS 7 and later—it will return `NULL` and log a sandbox violation in `syslog`. See [`Concurrency Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091) for possible replacement technologies.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `name`: The name with which to register the port.   can be  .
- `callout`: The callback function invoked when a message is received on the message port.
- `context`: A structure holding contextual information for the message port. The function copies the information out of the structure, so the memory pointed to by   does not need to persist beyond the function call.
- `shouldFreeInfo`: A flag set by the function to indicate whether the   member of   should be freed. The flag is set to   on failure or if a local port named   already exists,   otherwise.   can be  .

## See Also

- [func CFMessagePortCreateRemote(CFAllocator!, CFString!) -> CFMessagePort!](cfmessageportcreateremote(_:_:).md)
  Returns a CFMessagePort object connected to a remote port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportcreatelocal(_:_:_:_:_:))*