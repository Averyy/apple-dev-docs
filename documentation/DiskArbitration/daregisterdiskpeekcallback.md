# DARegisterDiskPeekCallback(_:_:_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func

Registers a callback function to be called whenever a disk has been probed.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DARegisterDiskPeekCallback(_ session: DASession, _ match: CFDictionary?, _ order: CFIndex, _ callback: DADiskPeekCallback, _ context: UnsafeMutableRawPointer?)
```

## Parameters

- `session`: The session object.
- `match`: The disk description keys to match. Pass NULL for all disk objects.
- `order`: The callback order, from lowest to highest. Pass 0 for the default.
- `callback`: The callback function to call when a disk has been probed.
- `context`: The user-defined context parameter to pass to the callback function.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/daregisterdiskpeekcallback(_:_:_:_:_:))*