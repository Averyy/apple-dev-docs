# DADiskCopyWholeDisk(_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Obtain the associated whole disk object for the specified disk.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADiskCopyWholeDisk(_ disk: DADisk) -> DADisk?
```

```c
extern DADiskRefDADiskCopyWholeDisk(DADiskRef disk);
```

#### Return Value

The disk’s associated whole disk object.

#### Discussion

The caller of this function receives a reference to the returned object. The caller also implicitly retains the object and is responsible for releasing it with CFRelease().

## Parameters

- `disk`: The disk object.

## See Also

### Miscellaneous
- [func DADiskCopyDescription(DADisk) -> CFDictionary?](./dadiskcopydescription%28_%29.md)
  Obtains the Disk Arbitration description of the specified disk.
- [func DADiskCopyIOMedia(DADisk) -> io_service_t](./dadiskcopyiomedia%28_%29.md)
  Obtains the I/O Kit media object for the specified disk.
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

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskcopywholedisk(_:))*