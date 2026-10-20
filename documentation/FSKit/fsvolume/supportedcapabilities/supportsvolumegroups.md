# supportsVolumeGroups

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates whether the volume supports volume groups.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportsVolumeGroups: Bool { get set }
```

```objc
@property (nonatomic) BOOL supportsVolumeGroups;
```

#### Discussion

Volume groups involve multiple logical file systems that the system can mount and unmount together, and for which the system can present common file system identifier information.

## See Also

### Declaring volume capabilities
- [var supportsSharedSpace: Bool](./supportssharedspace.md)
  A Boolean property that indicates whether the volume supports multiple logical file systems that share space in a single “partition.”
- [var doesNotSupportVolumeSizes: Bool](./doesnotsupportvolumesizes.md)
  A Boolean property that indicates the volume doesn’t support certain volume size reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supportsvolumegroups)*