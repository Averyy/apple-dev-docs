# doesNotSupportImmutableFiles

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates the volume doesn’t support immutable files.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var doesNotSupportImmutableFiles: Bool { get set }
```

```objc
@property (nonatomic) BOOL doesNotSupportImmutableFiles;
```

#### Discussion

A `true` value means this volume doesn’t support setting the `UF_IMMUTABLE` flag.

## See Also

### Declaring file capabilities
- [var supportsSparseFiles: Bool](./supportssparsefiles.md)
  A Boolean property that indicates whether the volume supports sparse files.
- [var supportsZeroRuns: Bool](./supportszeroruns.md)
  A Boolean property that indicates whether the volume supports zero runs
- [var supportsFastStatFS: Bool](./supportsfaststatfs.md)
  A Boolean property that indicates whether the volume supports fast results when fetching file system statistics.
- [var supports2TBFiles: Bool](./supports2tbfiles.md)
  A Boolean property that indicates whether the volume supports file sizes larger than 4GB, and potentially up to 2TB.
- [var supportsOpenDenyModes: Bool](./supportsopendenymodes.md)
  A Boolean property that indicates whether the volume supports open deny modes.
- [var supportsHiddenFiles: Bool](./supportshiddenfiles.md)
  A Boolean property that indicates whether the volume supports hidden files.
- [var doesNotSupportSettingFilePermissions: Bool](./doesnotsupportsettingfilepermissions.md)
  A Boolean property that indicates the volume doesn’t set file permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/doesnotsupportimmutablefiles)*