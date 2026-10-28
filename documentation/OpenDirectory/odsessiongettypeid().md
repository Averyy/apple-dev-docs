# ODSessionGetTypeID()

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Returns the type ID for a session.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODSessionGetTypeID() -> CFTypeID
```

```c
extern CFTypeID ODSessionGetTypeID();
```

## Return Value

The type ID for a session.

## See Also

### Working with Sessions
- [func ODSessionCopyNodeNames(CFAllocator!, ODSessionRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odsessioncopynodenames%28_,_,_%29.md)
  Returns the names of nodes registered in a given session.
- [func ODSessionCreate(CFAllocator!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>!](./odsessioncreate%28_,_,_%29.md)
  Creates a session to be passed to node functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsessiongettypeid())*