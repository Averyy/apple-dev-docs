# DADiskCreateFromVolumePath(_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func

Creates a new disk object.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func DADiskCreateFromVolumePath(_ allocator: CFAllocator?, _ session: DASession, _ path: CFURL) -> DADisk?
```

#### Return Value

A reference to a new DADisk.

#### Discussion

The caller of this function receives a reference to the returned object. The caller also implicitly retains the object and is responsible for releasing it with CFRelease().

## Parameters

- `allocator`: The allocator object to be used to allocate memory.
- `session`: The DASession in which to contact Disk Arbitration.
- `path`: The BSD mount point.

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
- [func DADiskGetBSDName(DADisk) -> UnsafePointer<CChar>?](dadiskgetbsdname(_:).md)
  Obtains the BSD device name for the specified disk.
- [func DADiskGetTypeID() -> CFTypeID](dadiskgettypeid().md)
  Returns the type identifier of all DADisk instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskcreatefromvolumepath(_:_:_:))*