# DADiskCopyDescription(_:)

**Framework**: Disk Arbitration  
**Kind**: func

Obtains the Disk Arbitration description of the specified disk.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADiskCopyDescription(_ disk: DADisk) -> CFDictionary?
```

#### Return Value

The disk’s Disk Arbitration description.

#### Discussion

This function will contact Disk Arbitration to acquire the latest description of the specified disk, unless this function is called on a disk object passed within the context of a registered callback, in which case the description is current as of that callback event.

The caller of this function receives a reference to the returned object. The caller also implicitly retains the object and is responsible for releasing it with CFRelease().

## Parameters

- `disk`: The DADisk for which to obtain the Disk Arbitration description.

## See Also

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
- [func DADiskGetTypeID() -> CFTypeID](dadiskgettypeid().md)
  Returns the type identifier of all DADisk instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskcopydescription(_:))*