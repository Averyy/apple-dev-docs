# supportsSharedSpace

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates whether the volume supports multiple logical file systems that share space in a single “partition.”

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportsSharedSpace: Bool { get set }
```

```objc
@property (nonatomic) BOOL supportsSharedSpace;
```

## See Also

### Declaring volume capabilities
- [var supportsVolumeGroups: Bool](./supportsvolumegroups.md)
  A Boolean property that indicates whether the volume supports volume groups.
- [var doesNotSupportVolumeSizes: Bool](./doesnotsupportvolumesizes.md)
  A Boolean property that indicates the volume doesn’t support certain volume size reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supportssharedspace)*