# DADiskUnmountApprovalCallback

**Framework**: Disk Arbitration  
**Kind**: typealias

Type of the callback function used by DARegisterDiskUnmountApprovalCallback().

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
typealias DADiskUnmountApprovalCallback = (DADisk, UnsafeMutableRawPointer?) -> Unmanaged<DADissenter>?
```

#### Return Value

A dissenter reference. Pass NULL to approve.

#### Discussion

The caller of this callback receives a reference to the returned object. The caller also implicitly retains the object and is responsible for releasing it with CFRelease().

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
- [typealias DADiskPeekCallback](dadiskpeekcallback.md)
  Type of the callback function used by DARegisterDiskPeekCallback().
- [typealias DADiskRenameCallback](dadiskrenamecallback.md)
  Type of the callback function used by DADiskRename().
- [typealias DADiskUnmountCallback](dadiskunmountcallback.md)
  Type of the callback function used by DADiskUnmount().


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskunmountapprovalcallback)*