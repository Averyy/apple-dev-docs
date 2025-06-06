# ODSessionGetTypeID()

**Framework**: Open Directory  
**Kind**: func

Returns the type ID for a session.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODSessionGetTypeID() -> CFTypeID
```

#### Return Value

The type ID for a session.

## See Also

- [func ODSessionCopyNodeNames(CFAllocator!, ODSessionRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odsessioncopynodenames(_:_:_:).md)
  Returns the names of nodes registered in a given session.
- [func ODSessionCreate(CFAllocator!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>!](odsessioncreate(_:_:_:).md)
  Creates a session to be passed to node functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsessiongettypeid())*