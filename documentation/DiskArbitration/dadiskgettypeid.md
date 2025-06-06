# DADiskGetTypeID()

**Framework**: Disk Arbitration  
**Kind**: func

Returns the type identifier of all DADisk instances.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADiskGetTypeID() -> CFTypeID
```

## See Also

- [func DADiskCopyDescription(DADisk) -> CFDictionary?](dadiskcopydescription(_:).md)
  Obtains the Disk Arbitration description of the specified disk.
- [func DADiskCopyIOMedia(DADisk) -> io_service_t](dadiskcopyiomedia(_:).md)
  Obtains the I/O Kit media object for the specified disk.
- [func DADiskCopyWholeDisk(DADisk) -> DADisk?](dadiskcopywholedisk(_:).md)
  Obtain the associated whole disk object for the specified disk.
- [func DADiskCreateFromBSDName(CFAllocator?, DASession, UnsafePointer<CChar>) -> DADisk?](dadiskcreatefrombsdname(_:_:_:).md)
  Creates a new disk object.
- [func DADiskCreateFromIOMedia(CFAllocator?, DASession, io_service_t) -> DADisk?](dadiskcreatefromiomedia(_:_:_:).md)
  Creates a new disk object.
- [func DADiskCreateFromVolumePath(CFAllocator?, DASession, CFURL) -> DADisk?](dadiskcreatefromvolumepath(_:_:_:).md)
  Creates a new disk object.
- [func DADiskGetBSDName(DADisk) -> UnsafePointer<CChar>?](dadiskgetbsdname(_:).md)
  Obtains the BSD device name for the specified disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskgettypeid())*