# DADiskCreateFromVolumePath(_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Creates a new disk object.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func DADiskCreateFromVolumePath(_ allocator: CFAllocator?, _ session: DASession, _ path: CFURL) -> DADisk?
```

```c
extern DADiskRefDADiskCreateFromVolumePath(CFAllocatorRef allocator, DASessionRef session, CFURLRef path);
```

## Return Value

A reference to a new DADisk.

## Discussion

The caller of this function receives a reference to the returned object. The caller also implicitly retains the object and is responsible for releasing it with CFRelease().

## Parameters

- `allocator`: The allocator object to be used to allocate memory.
- `session`: The DASession in which to contact Disk Arbitration.
- `path`: The BSD mount point.

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
- [func DADiskGetBSDName(DADisk) -> UnsafePointer<CChar>?](./dadiskgetbsdname%28_%29.md)
  Obtains the BSD device name for the specified disk.
- [func DADiskGetTypeID() -> CFTypeID](./dadiskgettypeid%28%29.md)
  Returns the type identifier of all DADisk instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskcreatefromvolumepath(_:_:_:))*