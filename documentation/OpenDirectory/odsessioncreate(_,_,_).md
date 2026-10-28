# ODSessionCreate(_:_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Creates a session to be passed to node functions.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODSessionCreate(_ allocator: CFAllocator!, _ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>!
```

```c
extern ODSessionRefODSessionCreate(CFAllocatorRef allocator, CFDictionaryRef options, CFErrorRef*error);
```

## Return Value

The created session.

## Parameters

- `allocator`: The memory allocator to use. If `NULL`, the default allocator is used.
- `options`: A dictionary of options to associate with the session.
- `error`: An error reference for error details. Can be `NULL`.

## See Also

### Related Documentation
- [Session Keys](./session-keys.md)
  Keys used when specifying session information.
### Working with Sessions
- [func ODSessionCopyNodeNames(CFAllocator!, ODSessionRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odsessioncopynodenames%28_,_,_%29.md)
  Returns the names of nodes registered in a given session.
- [func ODSessionGetTypeID() -> CFTypeID](./odsessiongettypeid%28%29.md)
  Returns the type ID for a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsessioncreate(_:_:_:))*