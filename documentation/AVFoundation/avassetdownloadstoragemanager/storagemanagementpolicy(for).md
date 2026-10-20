# storageManagementPolicy(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns the storage management policy for a downloaded asset.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func storageManagementPolicy(for downloadStorageURL: URL) -> AVAssetDownloadStorageManagementPolicy?
```

#### Return Value

The storage management policy for the asset, or `nil` if one isn’t set.

## Parameters

- `downloadStorageURL`: The location of the downloaded asset.

## See Also

- [func setStorageManagementPolicy(AVAssetDownloadStorageManagementPolicy, for: URL)](avassetdownloadstoragemanager/setstoragemanagementpolicy(_:for:).md)
  Sets a storage policy for the downloaded asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager/storagemanagementpolicy(for:))*