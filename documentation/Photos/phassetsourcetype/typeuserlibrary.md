# typeUserLibrary

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

The asset is part of the user’s main Photos library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var typeUserLibrary: PHAssetSourceType { get }
```

```c
PHAssetSourceTypeUserLibrary
```

## Discussion

The main library contains both assets that originate on the device (such as photos and videos captured with the Camera app or screenshots) and assets synchronized through iCloud Photo Library or My Photo Stream. These assets appear in Moments collections and can be edited or deleted.

## See Also

### Constants
- [static var typeCloudShared: PHAssetSourceType](./typecloudshared.md)
  The asset originates from an iCloud Shared Album.
- [static var typeiTunesSynced: PHAssetSourceType](./typeitunessynced.md)
  The asset originates from a Mac or PC and is present on the device through iTunes sync.
- [PHAssetSourceTypeNone](./phassetsourcetypenone.md)
  Source information is not available for the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetsourcetype/typeuserlibrary)*