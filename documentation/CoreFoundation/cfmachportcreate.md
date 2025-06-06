# CFMachPortCreate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFMachPort object with a new Mach port.

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
func CFMachPortCreate(_ allocator: CFAllocator!, _ callout: CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>!, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!
```

#### Return Value

The new CFMachPort object or `NULL` on failure. The CFMachPort object has both send and receive rights. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `callout`: The callback function invoked when a message is received on the new Mach port.
- `context`: A structure holding contextual information for the new Mach port. The function copies the information out of the structure, so the memory pointed to by   does not need to persist beyond the function call.
- `shouldFreeInfo`: A flag set by the function to indicate whether the   member of   should be freed. The flag is set to   on failure,   otherwise.   can be  .

## See Also

- [func CFMachPortCreateWithPort(CFAllocator!, mach_port_t, CFMachPortCallBack!, UnsafeMutablePointer<CFMachPortContext>!, UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!](cfmachportcreatewithport(_:_:_:_:_:).md)
  Creates a CFMachPort object for a pre-existing native Mach port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportcreate(_:_:_:_:))*