# AVMutableAssetDownloadStorageManagementPolicy

**Framework**: AVFoundation  
**Kind**: class

A mutable object that you use to create a new storage management policy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class AVMutableAssetDownloadStorageManagementPolicy
```

## Topics

### Managing Storage
- [var expirationDate: Date](avmutableassetdownloadstoragemanagementpolicy/expirationdate.md)
  The expiration date for an asset.
- [var priority: AVAssetDownloadedAssetEvictionPriority](avmutableassetdownloadstoragemanagementpolicy/priority.md)
  The eviction priority for a downloaded asset.
- [struct AVAssetDownloadedAssetEvictionPriority](avassetdownloadedassetevictionpriority.md)
  Constants that define eviction priorities for a storage management policy.

## Relationships

### Inherits From
- [AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAssetDownloadStorageManager](avassetdownloadstoragemanager.md)
  An object that manages policies to automatically purge downloaded assets.
- [class AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md)
  An object that defines a policy to automatically manage the storage of downloaded assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableassetdownloadstoragemanagementpolicy)*