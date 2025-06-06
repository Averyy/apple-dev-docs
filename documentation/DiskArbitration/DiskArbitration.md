# Disk Arbitration

**Framework**: Disk Arbitration  
**Kind**: module

Provides mechanisms to register and block disk mount or unmount events.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

#### Overview

For related documentation, see [`Mac Technology Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/About/About.html#//apple_ref/doc/uid/TP40001067).

## Topics

### Reference
- [DADisk.h](dadisk-h.md)
- [DADissenter.h](dadissenter-h.md)
- [DASession.h](dasession-h.md)
- [DiskArbitration.h](diskarbitration-h.md)
  Register for mount/unmount notifications, and block mount/unmount events.
- [DiskArbitration Enumerations](diskarbitration-enumerations.md)
- [DiskArbitration Constants](diskarbitration-constants.md)
- [DiskArbitration Functions](diskarbitration-functions.md)
- [DiskArbitration Data Types](diskarbitration-data-types.md)
### Articles
- [kDADiskOptionEjectUponLogout](kdadiskoptionejectuponlogout.md)
- [kDADiskOptionMountAutomatic](kdadiskoptionmountautomatic.md)
- [kDADiskOptionMountAutomaticNoDefer](kdadiskoptionmountautomaticnodefer.md)
- [kDADiskOptionPrivate](kdadiskoptionprivate.md)
- [DAReturn](enum_(unnamed)-3ky11.md)
  A return code.
### Variables
- [let kDADiskDescriptionFSKitPrefix: CFString](kdadiskdescriptionfskitprefix.md)
- [var kDADiskMountOptionNoFollow: Int](kdadiskmountoptionnofollow.md)
- [var kDAReturnBadArgument: Int](kdareturnbadargument.md)
- [var kDAReturnBusy: Int](kdareturnbusy.md)
- [var kDAReturnError: Int](kdareturnerror.md)
- [var kDAReturnExclusiveAccess: Int](kdareturnexclusiveaccess.md)
- [var kDAReturnNoResources: Int](kdareturnnoresources.md)
- [var kDAReturnNotFound: Int](kdareturnnotfound.md)
- [var kDAReturnNotMounted: Int](kdareturnnotmounted.md)
- [var kDAReturnNotPermitted: Int](kdareturnnotpermitted.md)
- [var kDAReturnNotPrivileged: Int](kdareturnnotprivileged.md)
- [var kDAReturnNotReady: Int](kdareturnnotready.md)
- [var kDAReturnNotWritable: Int](kdareturnnotwritable.md)
- [var kDAReturnSuccess: Int](kdareturnsuccess.md)
- [var kDAReturnUnsupported: Int](kdareturnunsupported.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/DiskArbitration)*