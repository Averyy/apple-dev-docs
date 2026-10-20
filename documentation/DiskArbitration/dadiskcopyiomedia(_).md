# DADiskCopyIOMedia(_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Obtains the I/O Kit media object for the specified disk.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADiskCopyIOMedia(_ disk: DADisk) -> io_service_t
```

```c
extern io_service_t DADiskCopyIOMedia(DADiskRef disk);
```

#### Return Value

The disk’s I/O Kit media object.

#### Discussion

The caller of this function receives a reference to the returned object. The caller also implicitly retains the object and is responsible for releasing it with IOObjectRelease().

## Parameters

- `disk`: The DADisk for which to obtain the I/O Kit media object.

## See Also

### Miscellaneous
- [func DADiskCopyDescription(DADisk) -> CFDictionary?](./dadiskcopydescription%28_%29.md)
  Obtains the Disk Arbitration description of the specified disk.
- [func DADiskCopyWholeDisk(DADisk) -> DADisk?](./dadiskcopywholedisk%28_%29.md)
  Obtain the associated whole disk object for the specified disk.
- [func DADiskCreateFromBSDName(CFAllocator?, DASession, UnsafePointer<CChar>) -> DADisk?](./dadiskcreatefrombsdname%28_,_,_%29.md)
  Creates a new disk object.
- [func DADiskCreateFromIOMedia(CFAllocator?, DASession, io_service_t) -> DADisk?](./dadiskcreatefromiomedia%28_,_,_%29.md)
  Creates a new disk object.
- [func DADiskCreateFromVolumePath(CFAllocator?, DASession, CFURL) -> DADisk?](./dadiskcreatefromvolumepath%28_,_,_%29.md)
  Creates a new disk object.
- [func DADiskGetBSDName(DADisk) -> UnsafePointer<CChar>?](./dadiskgetbsdname%28_%29.md)
  Obtains the BSD device name for the specified disk.
- [func DADiskGetTypeID() -> CFTypeID](./dadiskgettypeid%28%29.md)
  Returns the type identifier of all DADisk instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskcopyiomedia(_:))*