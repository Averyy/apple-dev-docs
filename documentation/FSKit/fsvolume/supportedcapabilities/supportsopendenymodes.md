# supportsOpenDenyModes

**Framework**: FSKit  
**Kind**: property

A Boolean property that indicates whether the volume supports open deny modes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportsOpenDenyModes: Bool { get set }
```

#### Discussion

These are modes such as “open for read write, deny write”.

## See Also

- [var supportsSparseFiles: Bool](fsvolume/supportedcapabilities/supportssparsefiles.md)
  A Boolean property that indicates whether the volume supports sparse files.
- [var supportsZeroRuns: Bool](fsvolume/supportedcapabilities/supportszeroruns.md)
  A Boolean property that indicates whether the volume supports zero runs
- [var supportsFastStatFS: Bool](fsvolume/supportedcapabilities/supportsfaststatfs.md)
  A Boolean property that indicates whether the volume supports fast results when fetching file system statistics.
- [var supports2TBFiles: Bool](fsvolume/supportedcapabilities/supports2tbfiles.md)
  A Boolean property that indicates whether the volume supports file sizes larger than 4GB, and potentially up to 2TB.
- [var supportsHiddenFiles: Bool](fsvolume/supportedcapabilities/supportshiddenfiles.md)
  A Boolean property that indicates whether the volume supports hidden files.
- [var doesNotSupportImmutableFiles: Bool](fsvolume/supportedcapabilities/doesnotsupportimmutablefiles.md)
  A Boolean property that indicates the volume doesn’t support immutable files.
- [var doesNotSupportSettingFilePermissions: Bool](fsvolume/supportedcapabilities/doesnotsupportsettingfilepermissions.md)
  A Boolean property that indicates the volume doesn’t set file permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supportsopendenymodes)*