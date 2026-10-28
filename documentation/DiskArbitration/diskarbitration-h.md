# DiskArbitration.h

**Framework**: Disk Arbitration  
**Role**: API Collection

Register for mount/unmount notifications, and block mount/unmount events.

## Overview

See the Overview section above for header-level documentation.

## Overview

### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <DiskArbitration/DADisk.h>
- <DiskArbitration/DADissenter.h>
- <DiskArbitration/DASession.h>

## Topics

### Miscellaneous
- [func DADiskClaim(DADisk, DADiskClaimOptions, DADiskClaimReleaseCallback?, UnsafeMutableRawPointer?, DADiskClaimCallback?, UnsafeMutableRawPointer?)](./dadiskclaim%28_,_,_,_,_,_%29.md)
  Claims the specified disk object for exclusive use.
- [func DADiskEject(DADisk, DADiskEjectOptions, DADiskEjectCallback?, UnsafeMutableRawPointer?)](./dadiskeject%28_,_,_,_%29.md)
  Ejects the specified disk object.
- [func DADiskGetOptions(DADisk) -> DADiskOptions](./dadiskgetoptions%28_%29.md)
  Obtains the options for the specified disk.
- [func DADiskIsClaimed(DADisk) -> Bool](./dadiskisclaimed%28_%29.md)
  Reports whether or not the disk is claimed.
- [func DADiskMount(DADisk, CFURL?, DADiskMountOptions, DADiskMountCallback?, UnsafeMutableRawPointer?)](./dadiskmount%28_,_,_,_,_%29.md)
  Mounts the volume at the specified disk object.
- [func DADiskMountWithArguments(DADisk, CFURL?, DADiskMountOptions, DADiskMountCallback?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFString>?>?)](./dadiskmountwitharguments%28_,_,_,_,_,_%29.md)
  Mounts the volume at the specified disk object, with the specified mount options.
- [func DADiskRename(DADisk, CFString, DADiskRenameOptions, DADiskRenameCallback?, UnsafeMutableRawPointer?)](./dadiskrename%28_,_,_,_,_%29.md)
  Renames the volume at the specified disk object.
- [func DADiskSetOptions(DADisk, DADiskOptions, Bool) -> DAReturn](./dadisksetoptions%28_,_,_%29.md)
  Sets the options for the specified disk.
- [func DADiskUnclaim(DADisk)](./dadiskunclaim%28_%29.md)
  Unclaims the specified disk object.
- [func DADiskUnmount(DADisk, DADiskUnmountOptions, DADiskUnmountCallback?, UnsafeMutableRawPointer?)](./dadiskunmount%28_,_,_,_%29.md)
  Unmounts the volume at the specified disk object.
- [func DARegisterDiskAppearedCallback(DASession, CFDictionary?, DADiskAppearedCallback, UnsafeMutableRawPointer?)](./daregisterdiskappearedcallback%28_,_,_,_%29.md)
  Registers a callback function to be called whenever a disk has appeared.
- [func DARegisterDiskDescriptionChangedCallback(DASession, CFDictionary?, CFArray?, DADiskDescriptionChangedCallback, UnsafeMutableRawPointer?)](./daregisterdiskdescriptionchangedcallback%28_,_,_,_,_%29.md)
  Registers a callback function to be called whenever a disk description has changed.
- [func DARegisterDiskDisappearedCallback(DASession, CFDictionary?, DADiskDisappearedCallback, UnsafeMutableRawPointer?)](./daregisterdiskdisappearedcallback%28_,_,_,_%29.md)
  Registers a callback function to be called whenever a disk has disappeared.
- [func DARegisterDiskEjectApprovalCallback(DASession, CFDictionary?, DADiskEjectApprovalCallback, UnsafeMutableRawPointer?)](./daregisterdiskejectapprovalcallback%28_,_,_,_%29.md)
  Registers a callback function to be called whenever a volume is to be ejected.
- [func DARegisterDiskMountApprovalCallback(DASession, CFDictionary?, DADiskMountApprovalCallback, UnsafeMutableRawPointer?)](./daregisterdiskmountapprovalcallback%28_,_,_,_%29.md)
  Registers a callback function to be called whenever a volume is to be mounted.
- [func DARegisterDiskPeekCallback(DASession, CFDictionary?, CFIndex, DADiskPeekCallback, UnsafeMutableRawPointer?)](./daregisterdiskpeekcallback%28_,_,_,_,_%29.md)
  Registers a callback function to be called whenever a disk has been probed.
- [func DARegisterDiskUnmountApprovalCallback(DASession, CFDictionary?, DADiskUnmountApprovalCallback, UnsafeMutableRawPointer?)](./daregisterdiskunmountapprovalcallback%28_,_,_,_%29.md)
  Registers a callback function to be called whenever a volume is to be unmounted.
- [func DAUnregisterCallback(DASession, UnsafeMutableRawPointer, UnsafeMutableRawPointer?)](./daunregistercallback%28_,_,_%29.md)
  Unregisters a registered callback function.
- [DAUnregisterApprovalCallback](./daunregisterapprovalcallback.md)
  Unregisters a registered callback function.
### Callbacks
- [typealias DADiskAppearedCallback](./dadiskappearedcallback.md)
  Type of the callback function used by DARegisterDiskAppearedCallback().
- [typealias DADiskClaimCallback](./dadiskclaimcallback.md)
  Type of the callback function used by DADiskClaim().
- [typealias DADiskClaimReleaseCallback](./dadiskclaimreleasecallback.md)
  Type of the callback function used by DADiskClaim().
- [typealias DADiskDescriptionChangedCallback](./dadiskdescriptionchangedcallback.md)
  Type of the callback function used by DARegisterDiskDescriptionChangedCallback().
- [typealias DADiskDisappearedCallback](./dadiskdisappearedcallback.md)
  Type of the callback function used by DARegisterDiskDisappearedCallback().
- [typealias DADiskEjectApprovalCallback](./dadiskejectapprovalcallback.md)
  Type of the callback function used by DARegisterDiskEjectApprovalCallback().
- [typealias DADiskEjectCallback](./dadiskejectcallback.md)
  Type of the callback function used by DADiskEject().
- [typealias DADiskMountApprovalCallback](./dadiskmountapprovalcallback.md)
  Type of the callback function used by DARegisterDiskMountApprovalCallback().
- [typealias DADiskMountCallback](./dadiskmountcallback.md)
  Type of the callback function used by DADiskMount().
- [typealias DADiskPeekCallback](./dadiskpeekcallback.md)
  Type of the callback function used by DARegisterDiskPeekCallback().
- [typealias DADiskRenameCallback](./dadiskrenamecallback.md)
  Type of the callback function used by DADiskRename().
- [typealias DADiskUnmountApprovalCallback](./dadiskunmountapprovalcallback.md)
  Type of the callback function used by DARegisterDiskUnmountApprovalCallback().
- [typealias DADiskUnmountCallback](./dadiskunmountcallback.md)
  Type of the callback function used by DADiskUnmount().
### Constants
- [Global Variables](./global-variables.md)
- [typealias DADiskClaimOptions](./dadiskclaimoptions.md)
  Options for DADiskClaim().
- [typealias DADiskEjectOptions](./dadiskejectoptions.md)
  Options for DADiskEject().
- [typealias DADiskMountOptions](./dadiskmountoptions.md)
  Options for DADiskMount().
- [typealias DADiskOptions](./dadiskoptions.md)
  Options for DADiskGetOptions() and DADiskSetOptions().
- [typealias DADiskRenameOptions](./dadiskrenameoptions.md)
  Options for DADiskRename().
- [typealias DADiskUnmountOptions](./dadiskunmountoptions.md)
  Options for DADiskUnmount().

## See Also

### Reference
- [DADisk.h](./dadisk-h.md)
- [DADissenter.h](./dadissenter-h.md)
- [DASession.h](./dasession-h.md)
- [DiskArbitration Enumerations](./diskarbitration-enumerations.md)
- [DiskArbitration Constants](./diskarbitration-constants.md)
- [DiskArbitration Data Types](./diskarbitration-data-types.md)
- [DiskArbitration Functions](./diskarbitration-functions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/diskarbitration-h)*