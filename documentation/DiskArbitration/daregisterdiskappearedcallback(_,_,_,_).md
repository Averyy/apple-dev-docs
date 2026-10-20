# DARegisterDiskAppearedCallback(_:_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Registers a callback function to be called whenever a disk has appeared.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DARegisterDiskAppearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskAppearedCallback, _ context: UnsafeMutableRawPointer?)
```

```c
extern void DARegisterDiskAppearedCallback(DASessionRef session, CFDictionaryRef match, DADiskAppearedCallback callback, void *context);
```

## Parameters

- `session`: The session object.
- `match`: The disk description keys to match. Pass NULL for all disk objects.
- `callback`: The callback function to call when a disk has appeared.
- `context`: The user-defined context parameter to pass to the callback function.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/daregisterdiskappearedcallback(_:_:_:_:))*