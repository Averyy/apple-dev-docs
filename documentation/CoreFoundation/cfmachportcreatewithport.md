# CFMachPortCreateWithPort(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFMachPort object for a pre-existing native Mach port.

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
func CFMachPortCreateWithPort(_ allocator: CFAllocator!, _ portNum: mach_port_t, _ callout: CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>!, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!
```

#### Return Value

The new CFMachPort object or `NULL` on failure. If a CFMachPort object already exists for `portNum`, the function returns the pre-existing object instead of creating a new object; the `context` and `callout` parameters are ignored in this case. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The CFMachPort object does not take full ownership of the send and receive rights of the Mach port `portNum`. It is the caller’s responsibility to deallocate the Mach port rights after the CFMachPort object is no longer needed and has been invalidated.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `portNum`: The native Mach port to use.
- `callout`: The callback function invoked when a message is received on the Mach port.
- `context`: A structure holding contextual information for the Mach port. The function copies the information out of the structure, so the memory pointed to by   does not need to persist beyond the function call.
- `shouldFreeInfo`: A flag set by the function to indicate whether the   member of   should be freed. The flag is set to   on failure or if a CFMachPort object already exists for  ,   otherwise.   can be  .

## See Also

- [func CFMachPortCreate(CFAllocator!, CFMachPortCallBack!, UnsafeMutablePointer<CFMachPortContext>!, UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!](cfmachportcreate(_:_:_:_:).md)
  Creates a CFMachPort object with a new Mach port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportcreatewithport(_:_:_:_:_:))*