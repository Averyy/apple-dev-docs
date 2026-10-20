# AVAssetDownloadStorageManager

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAssetDownloadStorageManager : NSObject
```

## Topics

### Accessing the shared manager
- [class func shared() -> AVAssetDownloadStorageManager](./avassetdownloadstoragemanager/shared%28%29.md)
  Returns the shared storage manager instance.
### Setting the storage policy
- [func storageManagementPolicy(for: URL) -> AVAssetDownloadStorageManagementPolicy?](./avassetdownloadstoragemanager/storagemanagementpolicy%28for%29.md)
  Returns the storage management policy for a downloaded asset.
- [func setStorageManagementPolicy(AVAssetDownloadStorageManagementPolicy, for: URL)](./avassetdownloadstoragemanager/setstoragemanagementpolicy%28_,for%29.md)
  Sets a storage policy for the downloaded asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Offline storage management
- [class AVAssetDownloadStorageManagementPolicy](./avassetdownloadstoragemanagementpolicy.md)
  An object that defines a policy to automatically manage the storage of downloaded assets.
- [class AVMutableAssetDownloadStorageManagementPolicy](./avmutableassetdownloadstoragemanagementpolicy.md)
  A mutable object that you use to create a new storage management policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager)*