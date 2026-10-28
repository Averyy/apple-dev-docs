# supportsFastStatFS

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates whether the volume supports fast results when fetching file system statistics.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportsFastStatFS: Bool { get set }
```

```objc
@property (nonatomic) BOOL supportsFastStatFS;
```

## Discussion

A true value means this volume hints to upper layers to indicate that `statfs(2)` is fast enough that its results need not be cached by the caller.

## See Also

### Declaring file capabilities
- [var supportsSparseFiles: Bool](./supportssparsefiles.md)
  A Boolean property that indicates whether the volume supports sparse files.
- [var supportsZeroRuns: Bool](./supportszeroruns.md)
  A Boolean property that indicates whether the volume supports zero runs
- [var supports2TBFiles: Bool](./supports2tbfiles.md)
  A Boolean property that indicates whether the volume supports file sizes larger than 4GB, and potentially up to 2TB.
- [var supportsOpenDenyModes: Bool](./supportsopendenymodes.md)
  A Boolean property that indicates whether the volume supports open deny modes.
- [var supportsHiddenFiles: Bool](./supportshiddenfiles.md)
  A Boolean property that indicates whether the volume supports hidden files.
- [var doesNotSupportImmutableFiles: Bool](./doesnotsupportimmutablefiles.md)
  A Boolean property that indicates the volume doesn’t support immutable files.
- [var doesNotSupportSettingFilePermissions: Bool](./doesnotsupportsettingfilepermissions.md)
  A Boolean property that indicates the volume doesn’t set file permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supportsfaststatfs)*