# CFSocketCreateWithSocketSignature(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFSocket object using information from a CFSocketSignature structure.

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
func CFSocketCreateWithSocketSignature(_ allocator: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>!, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>!) -> CFSocket!
```

#### Return Value

The new CFSocket object, or `NULL` if an error occurred. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `signature`: A   identifying the communication protocol and address with which to create the CFSocket object.
- `callBackTypes`: A bitwise-OR combination of the types of socket activity that should cause   to be called. See   for the possible activity values.
- `callout`: The function to call when one of the activities indicated by   occurs.
- `context`: A structure holding contextual information for the CFSocket object. The function copies the information out of the structure, so the memory pointed to by   does not need to persist beyond the function call. Can be  .

## See Also

- [func CFSocketCreate(CFAllocator!, Int32, Int32, Int32, CFOptionFlags, CFSocketCallBack!, UnsafePointer<CFSocketContext>!) -> CFSocket!](cfsocketcreate(_:_:_:_:_:_:_:).md)
  Creates a CFSocket object of a specified protocol and type.
- [func CFSocketCreateConnectedToSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>!, CFOptionFlags, CFSocketCallBack!, UnsafePointer<CFSocketContext>!, CFTimeInterval) -> CFSocket!](cfsocketcreateconnectedtosocketsignature(_:_:_:_:_:_:).md)
  Creates a CFSocket object and opens a connection to a remote socket.
- [func CFSocketCreateWithNative(CFAllocator!, CFSocketNativeHandle, CFOptionFlags, CFSocketCallBack!, UnsafePointer<CFSocketContext>!) -> CFSocket!](cfsocketcreatewithnative(_:_:_:_:_:).md)
  Creates a CFSocket object for a pre-existing native socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcreatewithsocketsignature(_:_:_:_:_:))*