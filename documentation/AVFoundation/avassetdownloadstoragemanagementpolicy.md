# AVAssetDownloadStorageManagementPolicy

**Framework**: AVFoundation  
**Kind**: class

An object that defines a policy to automatically manage the storage of downloaded assets.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class AVAssetDownloadStorageManagementPolicy
```

## Topics

### Inspecting a policy
- [var expirationDate: Date](avassetdownloadstoragemanagementpolicy/expirationdate.md)
  The expiration date for an asset.
- [var priority: AVAssetDownloadedAssetEvictionPriority](avassetdownloadstoragemanagementpolicy/priority.md)
  The eviction priority for an asset.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class AVAssetDownloadStorageManager](avassetdownloadstoragemanager.md)
  An object that manages policies to automatically purge downloaded assets.
- [class AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md)
  A mutable object that you use to create a new storage management policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanagementpolicy)*