# AVAssetDownloadStorageManagementPolicy

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAssetDownloadStorageManagementPolicy : NSObject
```

## Topics

### Inspecting a policy
- [var expirationDate: Date](./avassetdownloadstoragemanagementpolicy/expirationdate.md)
  The expiration date for an asset.
- [var priority: AVAssetDownloadedAssetEvictionPriority](./avassetdownloadstoragemanagementpolicy/priority.md)
  The eviction priority for an asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVMutableAssetDownloadStorageManagementPolicy](./avmutableassetdownloadstoragemanagementpolicy.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Offline storage management
- [class AVAssetDownloadStorageManager](./avassetdownloadstoragemanager.md)
  An object that manages policies to automatically purge downloaded assets.
- [class AVMutableAssetDownloadStorageManagementPolicy](./avmutableassetdownloadstoragemanagementpolicy.md)
  A mutable object that you use to create a new storage management policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanagementpolicy)*