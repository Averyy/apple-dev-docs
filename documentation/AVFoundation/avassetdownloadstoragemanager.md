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

### Accessing the shared manager
- [class func shared() -> AVAssetDownloadStorageManager](avassetdownloadstoragemanager/shared.md)
  Returns the shared storage manager instance.
### Setting the storage policy
- [func storageManagementPolicy(for: URL) -> AVAssetDownloadStorageManagementPolicy?](avassetdownloadstoragemanager/storagemanagementpolicy(for:).md)
  Returns the storage management policy for a downloaded asset.
- [func setStorageManagementPolicy(AVAssetDownloadStorageManagementPolicy, for: URL)](avassetdownloadstoragemanager/setstoragemanagementpolicy(_:for:).md)
  Sets a storage policy for the downloaded asset.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md)
  An object that defines a policy to automatically manage the storage of downloaded assets.
- [class AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md)
  A mutable object that you use to create a new storage management policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager)*