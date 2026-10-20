# DADiskClaim(_:_:_:_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Claims the specified disk object for exclusive use.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADiskClaim(_ disk: DADisk, _ options: DADiskClaimOptions, _ release: DADiskClaimReleaseCallback?, _ releaseContext: UnsafeMutableRawPointer?, _ callback: DADiskClaimCallback?, _ callbackContext: UnsafeMutableRawPointer?)
```

```c
extern void DADiskClaim(DADiskRef disk, DADiskClaimOptions options, DADiskClaimReleaseCallback release, void *releaseContext, DADiskClaimCallback callback, void *callbackContext);
```

## Parameters

- `disk`: The disk object.
- `options`: The claim options.
- `release`: The callback function to call when the claim is to be released.
- `releaseContext`: The user-defined context parameter to pass to the callback function.
- `callback`: The callback function to call once the claim completes.
- `callbackContext`: The user-defined context parameter to pass to the callback function.

## See Also

### Miscellaneous
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskclaim(_:_:_:_:_:_:))*