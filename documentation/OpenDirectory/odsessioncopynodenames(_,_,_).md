# ODSessionCopyNodeNames(_:_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Returns the names of nodes registered in a given session.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODSessionCopyNodeNames(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!
```

```c
extern CFArrayRefODSessionCopyNodeNames(CFAllocatorRef allocator, ODSessionRef session, CFErrorRef*error);
```

## Return Value

An array of valid node names in the given session.

## Parameters

- `allocator`: The memory allocator to use. If `NULL`, the default allocator is used.
- `session`: The session.
- `error`: An error reference for error details. Can be `NULL`.

## See Also

### Working with Sessions
- [func ODSessionCreate(CFAllocator!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>!](./odsessioncreate%28_,_,_%29.md)
  Creates a session to be passed to node functions.
- [func ODSessionGetTypeID() -> CFTypeID](./odsessiongettypeid%28%29.md)
  Returns the type ID for a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsessioncopynodenames(_:_:_:))*