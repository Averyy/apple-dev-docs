# DADiskUnmountOptions

**Framework**: Disk Arbitration  
**Kind**: typealias

Options for DADiskUnmount().

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias DADiskUnmountOptions = UInt32
```

## Topics

### Constants
- [var kDADiskUnmountOptionForce: Int](kdadiskunmountoptionforce.md)
  Unmount the volume even if files are still active.
- [var kDADiskUnmountOptionWhole: Int](kdadiskunmountoptionwhole.md)
  Unmount the volumes tied to the whole disk object.

## See Also

- [typealias DADiskClaimOptions](dadiskclaimoptions.md)
  Options for DADiskClaim().
- [typealias DADiskEjectOptions](dadiskejectoptions.md)
  Options for DADiskEject().
- [typealias DADiskMountOptions](dadiskmountoptions.md)
  Options for DADiskMount().
- [typealias DADiskOptions](dadiskoptions.md)
  Options for DADiskGetOptions() and DADiskSetOptions().
- [typealias DADiskRenameOptions](dadiskrenameoptions.md)
  Options for DADiskRename().
- [typealias DAReturn](dareturn.md)
  A return code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadiskunmountoptions)*