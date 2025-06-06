# DADiskCopyIOMedia(_:)

**Framework**: Disk Arbitration  
**Kind**: func

Obtains the I/O Kit media object for the specified disk.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADiskCopyIOMedia(_ disk: DADisk) -> io_service_t
```

#### Return Value

The disk’s I/O Kit media object.

#### Discussion

The caller of this function receives a reference to the returned object. The caller also implicitly retains the object and is responsible for releasing it with IOObjectRelease().

## Parameters

- `disk`: The DADisk for which to obtain the I/O Kit media object.

## See Also

- [func DADiskCopyDescription(DADisk) -> CFDictionary?](dadiskcopydescription(_:).md)
  Obtains the Disk Arbitration description of the specified disk.
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
- [func DADiskGetTypeID() -> CFTypeID](dadiskgettypeid().md)
  Returns the type identifier of all DADisk instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskcopyiomedia(_:))*