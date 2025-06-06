# DADiskMountWithArguments(_:_:_:_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func

Mounts the volume at the specified disk object, with the specified mount options.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADiskMountWithArguments(_ disk: DADisk, _ path: CFURL?, _ options: DADiskMountOptions, _ callback: DADiskMountCallback?, _ context: UnsafeMutableRawPointer?, _ arguments: UnsafeMutablePointer<Unmanaged<CFString>?>?)
```

## Parameters

- `disk`: The disk object.
- `path`: The mount path. Pass NULL for a “standard” mount path.
- `options`: The mount options.
- `callback`: The callback function to call once the mount completes.
- `context`: The user-defined context parameter to pass to the callback function.
- `arguments`: The null-terminated list of mount options to pass to /sbin/mount -o.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskmountwitharguments(_:_:_:_:_:_:))*