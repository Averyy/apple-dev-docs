# setStorageManagementPolicy(_:for:)

**Framework**: AVFoundation  
**Kind**: method

Sets a storage policy for the downloaded asset.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func setStorageManagementPolicy(_ storageManagementPolicy: AVAssetDownloadStorageManagementPolicy, for downloadStorageURL: URL)
```

## Parameters

- `storageManagementPolicy`: The policy to set for the downloaded asset.
- `downloadStorageURL`: The location of the downloaded asset.

## See Also

- [func storageManagementPolicy(for: URL) -> AVAssetDownloadStorageManagementPolicy?](avassetdownloadstoragemanager/storagemanagementpolicy(for:).md)
  Returns the storage management policy for a downloaded asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager/setstoragemanagementpolicy(_:for:))*