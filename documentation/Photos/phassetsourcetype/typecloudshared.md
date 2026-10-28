# typeCloudShared

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

The asset originates from an iCloud Shared Album.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var typeCloudShared: PHAssetSourceType { get }
```

```c
PHAssetSourceTypeCloudShared
```

## Discussion

Assets from shared albums cannot be edited and do not appear in Moments collections.

## See Also

### Constants
- [static var typeUserLibrary: PHAssetSourceType](./typeuserlibrary.md)
  The asset is part of the user’s main Photos library.
- [static var typeiTunesSynced: PHAssetSourceType](./typeitunessynced.md)
  The asset originates from a Mac or PC and is present on the device through iTunes sync.
- [PHAssetSourceTypeNone](./phassetsourcetypenone.md)
  Source information is not available for the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetsourcetype/typecloudshared)*