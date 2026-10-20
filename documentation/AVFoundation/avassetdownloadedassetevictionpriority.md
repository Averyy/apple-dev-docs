# AVAssetDownloadedAssetEvictionPriority

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * AVAssetDownloadedAssetEvictionPriority;
```

## Topics

### Eviction priorities
- [static let `default`: AVAssetDownloadedAssetEvictionPriority](./avassetdownloadedassetevictionpriority/default.md)
  The default eviction priority.
- [static let important: AVAssetDownloadedAssetEvictionPriority](./avassetdownloadedassetevictionpriority/important.md)
  An eviction priority that indicates that this asset is important and the system should evict lower-priority assets first.
### Initializers
- [init(rawValue: String)](./avassetdownloadedassetevictionpriority/init%28rawvalue%29.md)
  Creates an eviction priority with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing storage
- [var expirationDate: Date](./avmutableassetdownloadstoragemanagementpolicy/expirationdate.md)
  The expiration date for an asset.
- [var priority: AVAssetDownloadedAssetEvictionPriority](./avmutableassetdownloadstoragemanagementpolicy/priority.md)
  The eviction priority for a downloaded asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadedassetevictionpriority)*