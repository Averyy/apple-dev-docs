# AVAssetDownloadedAssetEvictionPriority

**Framework**: AVFoundation  
**Kind**: struct

Constants that define eviction priorities for a storage management policy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct AVAssetDownloadedAssetEvictionPriority
```

## Topics

### Eviction Priorities
- [static let `default`: AVAssetDownloadedAssetEvictionPriority](avassetdownloadedassetevictionpriority/default.md)
  The default eviction priority.
- [static let important: AVAssetDownloadedAssetEvictionPriority](avassetdownloadedassetevictionpriority/important.md)
  An eviction priority that indicates that this asset is important and the system should evict lower-priority assets first.
### Initializers
- [init(rawValue: String)](avassetdownloadedassetevictionpriority/init(rawvalue:).md)
  Creates an eviction priority with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var expirationDate: Date](avmutableassetdownloadstoragemanagementpolicy/expirationdate.md)
  The expiration date for an asset.
- [var priority: AVAssetDownloadedAssetEvictionPriority](avmutableassetdownloadstoragemanagementpolicy/priority.md)
  The eviction priority for a downloaded asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadedassetevictionpriority)*