# DADiskGetBSDName(_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Obtains the BSD device name for the specified disk.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADiskGetBSDName(_ disk: DADisk) -> UnsafePointer<CChar>?
```

```c
extern const char *DADiskGetBSDName(DADiskRef disk);
```

#### Return Value

The disk’s BSD device name.

#### Discussion

The BSD device name can be used with opendev() to open the BSD device.

## Parameters

- `disk`: The DADisk for which to obtain the BSD device name.

## See Also

### Miscellaneous
- [func DADiskCopyDescription(DADisk) -> CFDictionary?](./dadiskcopydescription%28_%29.md)
  Obtains the Disk Arbitration description of the specified disk.
- [func DADiskCopyIOMedia(DADisk) -> io_service_t](./dadiskcopyiomedia%28_%29.md)
  Obtains the I/O Kit media object for the specified disk.
- [func DADiskCopyWholeDisk(DADisk) -> DADisk?](./dadiskcopywholedisk%28_%29.md)
  Obtain the associated whole disk object for the specified disk.
- [func DADiskCreateFromBSDName(CFAllocator?, DASession, UnsafePointer<CChar>) -> DADisk?](./dadiskcreatefrombsdname%28_,_,_%29.md)
  Creates a new disk object.
- [func DADiskCreateFromIOMedia(CFAllocator?, DASession, io_service_t) -> DADisk?](./dadiskcreatefromiomedia%28_,_,_%29.md)
  Creates a new disk object.
- [func DADiskCreateFromVolumePath(CFAllocator?, DASession, CFURL) -> DADisk?](./dadiskcreatefromvolumepath%28_,_,_%29.md)
  Creates a new disk object.
- [func DADiskGetTypeID() -> CFTypeID](./dadiskgettypeid%28%29.md)
  Returns the type identifier of all DADisk instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskgetbsdname(_:))*