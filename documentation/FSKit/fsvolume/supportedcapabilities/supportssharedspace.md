# supportsSharedSpace

**Framework**: FSKit  
**Kind**: property

A Boolean property that indicates whether the volume supports multiple logical file systems that share space in a single “partition.”

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportsSharedSpace: Bool { get set }
```

## See Also

- [var supportsVolumeGroups: Bool](fsvolume/supportedcapabilities/supportsvolumegroups.md)
  A Boolean property that indicates whether the volume supports volume groups.
- [var doesNotSupportVolumeSizes: Bool](fsvolume/supportedcapabilities/doesnotsupportvolumesizes.md)
  A Boolean property that indicates the volume doesn’t support certain volume size reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supportssharedspace)*