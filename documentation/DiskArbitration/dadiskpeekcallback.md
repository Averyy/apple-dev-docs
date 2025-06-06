# DADiskPeekCallback

**Framework**: Disk Arbitration  
**Kind**: typealias

Type of the callback function used by DARegisterDiskPeekCallback().

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
typealias DADiskPeekCallback = (DADisk, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

The peek callback functions are called in a specific order, from lowest order to highest order. DADiskClaim() could be used here to claim the disk object and DADiskSetOptions() could be used here to set up options on the disk object.

## Parameters

- `disk`: A disk object.
- `context`: The user-defined context parameter given to the registration function.

## See Also

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
- [typealias DADiskRenameCallback](dadiskrenamecallback.md)
  Type of the callback function used by DADiskRename().
- [typealias DADiskUnmountApprovalCallback](dadiskunmountapprovalcallback.md)
  Type of the callback function used by DARegisterDiskUnmountApprovalCallback().
- [typealias DADiskUnmountCallback](dadiskunmountcallback.md)
  Type of the callback function used by DADiskUnmount().


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskpeekcallback)*