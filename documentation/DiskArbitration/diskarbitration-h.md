# DiskArbitration.h

**Framework**: Disk Arbitration

Register for mount/unmount notifications, and block mount/unmount events.

#### Overview

See the Overview section above for header-level documentation.

#### Overview

##### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <DiskArbitration/DADisk.h>
- <DiskArbitration/DADissenter.h>
- <DiskArbitration/DASession.h>

## Topics

### Miscellaneous
- [func DADiskClaim(DADisk, DADiskClaimOptions, DADiskClaimReleaseCallback?, UnsafeMutableRawPointer?, DADiskClaimCallback?, UnsafeMutableRawPointer?)](dadiskclaim(_:_:_:_:_:_:).md)
  Claims the specified disk object for exclusive use.
- [func DADiskEject(DADisk, DADiskEjectOptions, DADiskEjectCallback?, UnsafeMutableRawPointer?)](dadiskeject(_:_:_:_:).md)
  Ejects the specified disk object.
- [func DADiskGetOptions(DADisk) -> DADiskOptions](dadiskgetoptions(_:).md)
  Obtains the options for the specified disk.
- [func DADiskIsClaimed(DADisk) -> Bool](dadiskisclaimed(_:).md)
  Reports whether or not the disk is claimed.
- [func DADiskMount(DADisk, CFURL?, DADiskMountOptions, DADiskMountCallback?, UnsafeMutableRawPointer?)](dadiskmount(_:_:_:_:_:).md)
  Mounts the volume at the specified disk object.
- [func DADiskMountWithArguments(DADisk, CFURL?, DADiskMountOptions, DADiskMountCallback?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFString>?>?)](dadiskmountwitharguments(_:_:_:_:_:_:).md)
  Mounts the volume at the specified disk object, with the specified mount options.
- [func DADiskRename(DADisk, CFString, DADiskRenameOptions, DADiskRenameCallback?, UnsafeMutableRawPointer?)](dadiskrename(_:_:_:_:_:).md)
  Renames the volume at the specified disk object.
- [func DADiskSetOptions(DADisk, DADiskOptions, Bool) -> DAReturn](dadisksetoptions(_:_:_:).md)
  Sets the options for the specified disk.
- [func DADiskUnclaim(DADisk)](dadiskunclaim(_:).md)
  Unclaims the specified disk object.
- [func DADiskUnmount(DADisk, DADiskUnmountOptions, DADiskUnmountCallback?, UnsafeMutableRawPointer?)](dadiskunmount(_:_:_:_:).md)
  Unmounts the volume at the specified disk object.
- [func DARegisterDiskAppearedCallback(DASession, CFDictionary?, DADiskAppearedCallback, UnsafeMutableRawPointer?)](daregisterdiskappearedcallback(_:_:_:_:).md)
  Registers a callback function to be called whenever a disk has appeared.
- [func DARegisterDiskDescriptionChangedCallback(DASession, CFDictionary?, CFArray?, DADiskDescriptionChangedCallback, UnsafeMutableRawPointer?)](daregisterdiskdescriptionchangedcallback(_:_:_:_:_:).md)
  Registers a callback function to be called whenever a disk description has changed.
- [func DARegisterDiskDisappearedCallback(DASession, CFDictionary?, DADiskDisappearedCallback, UnsafeMutableRawPointer?)](daregisterdiskdisappearedcallback(_:_:_:_:).md)
  Registers a callback function to be called whenever a disk has disappeared.
- [func DARegisterDiskEjectApprovalCallback(DASession, CFDictionary?, DADiskEjectApprovalCallback, UnsafeMutableRawPointer?)](daregisterdiskejectapprovalcallback(_:_:_:_:).md)
  Registers a callback function to be called whenever a volume is to be ejected.
- [func DARegisterDiskMountApprovalCallback(DASession, CFDictionary?, DADiskMountApprovalCallback, UnsafeMutableRawPointer?)](daregisterdiskmountapprovalcallback(_:_:_:_:).md)
  Registers a callback function to be called whenever a volume is to be mounted.
- [func DARegisterDiskPeekCallback(DASession, CFDictionary?, CFIndex, DADiskPeekCallback, UnsafeMutableRawPointer?)](daregisterdiskpeekcallback(_:_:_:_:_:).md)
  Registers a callback function to be called whenever a disk has been probed.
- [func DARegisterDiskUnmountApprovalCallback(DASession, CFDictionary?, DADiskUnmountApprovalCallback, UnsafeMutableRawPointer?)](daregisterdiskunmountapprovalcallback(_:_:_:_:).md)
  Registers a callback function to be called whenever a volume is to be unmounted.
- [func DAUnregisterCallback(DASession, UnsafeMutableRawPointer, UnsafeMutableRawPointer?)](daunregistercallback(_:_:_:).md)
  Unregisters a registered callback function.
### Callbacks
- [typealias DADiskAppearedCallback](dadiskappearedcallback.md)
  Type of the callback function used by DARegisterDiskAppearedCallback().
- [typealias DADiskClaimCallback](dadiskclaimcallback.md)
  Type of the callback function used by DADiskClaim().
- [typealias DADiskClaimReleaseCallback](dadiskclaimreleasecallback.md)
  Type of the callback function used by DADiskClaim().
- [typealias DADiskDescriptionChangedCallback](dadiskdescriptionchangedcallback.md)
  Type of the callback function used by DARegisterDiskDescriptionChangedCallback().
- [typealias DADiskDisappearedCallback](dadiskdisappearedcallback.md)
  Type of the callback function used by DARegisterDiskDisappearedCallback().
- [typealias DADiskEjectApprovalCallback](dadiskejectapprovalcallback.md)
  Type of the callback function used by DARegisterDiskEjectApprovalCallback().
- [typealias DADiskEjectCallback](dadiskejectcallback.md)
  Type of the callback function used by DADiskEject().
- [typealias DADiskMountApprovalCallback](dadiskmountapprovalcallback.md)
  Type of the callback function used by DARegisterDiskMountApprovalCallback().
- [typealias DADiskMountCallback](dadiskmountcallback.md)
  Type of the callback function used by DADiskMount().
- [typealias DADiskPeekCallback](dadiskpeekcallback.md)
  Type of the callback function used by DARegisterDiskPeekCallback().
- [typealias DADiskRenameCallback](dadiskrenamecallback.md)
  Type of the callback function used by DADiskRename().
- [typealias DADiskUnmountApprovalCallback](dadiskunmountapprovalcallback.md)
  Type of the callback function used by DARegisterDiskUnmountApprovalCallback().
- [typealias DADiskUnmountCallback](dadiskunmountcallback.md)
  Type of the callback function used by DADiskUnmount().
### Constants
- [Global Variables](global-variables.md)
- [DADiskClaimOptions](dadiskclaimoptions.md)
  Options for DADiskClaim().
- [DADiskEjectOptions](dadiskejectoptions.md)
  Options for DADiskEject().
- [typealias DADiskMountOptions](dadiskmountoptions.md)
  Options for DADiskMount().
- [typealias DADiskRenameOptions](dadiskrenameoptions.md)
  Options for DADiskRename().
- [typealias DADiskUnmountOptions](dadiskunmountoptions.md)
  Options for DADiskUnmount().

## See Also

- [DADisk.h](dadisk-h.md)
- [DADissenter.h](dadissenter-h.md)
- [DASession.h](dasession-h.md)
- [DiskArbitration Enumerations](diskarbitration-enumerations.md)
- [DiskArbitration Constants](diskarbitration-constants.md)
- [DiskArbitration Data Types](diskarbitration-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/diskarbitration-h)*