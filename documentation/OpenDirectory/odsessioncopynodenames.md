# ODSessionCopyNodeNames(_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Returns the names of nodes registered in a given session.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODSessionCopyNodeNames(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!
```

#### Return Value

An array of valid node names in the given session.

## Parameters

- `allocator`: The memory allocator to use. If  , the default allocator is used.
- `session`: The session.
- `error`: An error reference for error details. Can be  .

## See Also

- [func ODSessionCreate(CFAllocator!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>!](odsessioncreate(_:_:_:).md)
  Creates a session to be passed to node functions.
- [func ODSessionGetTypeID() -> CFTypeID](odsessiongettypeid().md)
  Returns the type ID for a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsessioncopynodenames(_:_:_:))*