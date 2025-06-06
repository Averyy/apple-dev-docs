# AVAssetDownloadStorageManager

**Framework**: AVFoundation  
**Kind**: class

An object that manages policies to automatically purge downloaded assets.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class AVAssetDownloadStorageManager
```

## Topics

### Accessing the Shared Manager
- [class func shared() -> AVAssetDownloadStorageManager](avassetdownloadstoragemanager/shared.md)
  Returns the shared storage manager instance.
### Setting the Storage Policy
- [func storageManagementPolicy(for: URL) -> AVAssetDownloadStorageManagementPolicy?](avassetdownloadstoragemanager/storagemanagementpolicy(for:).md)
  Returns the storage management policy for a downloaded asset.
- [func setStorageManagementPolicy(AVAssetDownloadStorageManagementPolicy, for: URL)](avassetdownloadstoragemanager/setstoragemanagementpolicy(_:for:).md)
  Sets a storage policy for the downloaded asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md)
  An object that defines a policy to automatically manage the storage of downloaded assets.
- [class AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md)
  A mutable object that you use to create a new storage management policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager)*