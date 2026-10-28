# doesNotSupportVolumeSizes

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates the volume doesn’t support certain volume size reports.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var doesNotSupportVolumeSizes: Bool { get set }
```

```objc
@property (nonatomic) BOOL doesNotSupportVolumeSizes;
```

## Discussion

A true value means the volume doesn’t support determining values for total data blocks, available blocks, or free blocks, as in `f_blocks`, `f_bavail`, and `f_bfree` in the struct `statFS` returned by `statfs(2)`.

## See Also

### Declaring volume capabilities
- [var supportsSharedSpace: Bool](./supportssharedspace.md)
  A Boolean property that indicates whether the volume supports multiple logical file systems that share space in a single “partition.”
- [var supportsVolumeGroups: Bool](./supportsvolumegroups.md)
  A Boolean property that indicates whether the volume supports volume groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/doesnotsupportvolumesizes)*