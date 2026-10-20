# setStorageManagementPolicy(_:for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setStorageManagementPolicy:(AVAssetDownloadStorageManagementPolicy *) storageManagementPolicy forURL:(NSURL *) downloadStorageURL;
```

## Parameters

- `storageManagementPolicy`: The policy to set for the downloaded asset.
- `downloadStorageURL`: The location of the downloaded asset.

## See Also

### Setting the storage policy
- [func storageManagementPolicy(for: URL) -> AVAssetDownloadStorageManagementPolicy?](./storagemanagementpolicy%28for%29.md)
  Returns the storage management policy for a downloaded asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager/setstoragemanagementpolicy(_:for:))*