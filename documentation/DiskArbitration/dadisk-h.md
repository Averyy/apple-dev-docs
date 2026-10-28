# DADisk.h

**Framework**: Disk Arbitration  
**Role**: API Collection

## Overview

See the Overview section above for header-level documentation.

## Overview

### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <IOKit/IOKitLib.h>
- <DiskArbitration/DASession.h>

## Topics

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
- [func DADiskGetBSDName(DADisk) -> UnsafePointer<CChar>?](./dadiskgetbsdname%28_%29.md)
  Obtains the BSD device name for the specified disk.
- [func DADiskGetTypeID() -> CFTypeID](./dadiskgettypeid%28%29.md)
  Returns the type identifier of all DADisk instances.
### Data Types
- [class DADisk](./dadisk.md)
  Type of a reference to DADisk instances.

## See Also

### Reference
- [DADissenter.h](./dadissenter-h.md)
- [DASession.h](./dasession-h.md)
- [DiskArbitration.h](./diskarbitration-h.md)
  Register for mount/unmount notifications, and block mount/unmount events.
- [DiskArbitration Enumerations](./diskarbitration-enumerations.md)
- [DiskArbitration Constants](./diskarbitration-constants.md)
- [DiskArbitration Data Types](./diskarbitration-data-types.md)
- [DiskArbitration Functions](./diskarbitration-functions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadisk-h)*