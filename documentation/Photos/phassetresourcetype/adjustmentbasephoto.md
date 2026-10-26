# PHAssetResourceType.adjustmentBasePhoto

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Provides an unaltered version of its photo asset for use in for use in reconstructing recent edits.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case adjustmentBasePhoto
```

```c
PHAssetResourceTypeAdjustmentBasePhoto
```

#### Discussion

When you edit an asset, you have the option of resuming the most recent edit made. This process uses a [`PHAdjustmentData`](../phadjustmentdata.md) object to describe the edit, and an extra copy of the photo data representing the state of the asset before the edit. For details, see [`PHAsset`](../phasset.md).

## See Also

### Resource Types
- [PHAssetResourceType.photo](./photo.md)
  Provides the original photo data for its asset.
- [PHAssetResourceType.video](./video.md)
  Provides the original video data for its asset.
- [PHAssetResourceType.audio](./audio.md)
  Provides the original audio data for its asset.
- [PHAssetResourceType.alternatePhoto](./alternatephoto.md)
  Provides photo data that isn’t the primary form of its asset.
- [PHAssetResourceType.fullSizePhoto](./fullsizephoto.md)
  Provides a modified version of the original photo asset.
- [PHAssetResourceType.fullSizeVideo](./fullsizevideo.md)
  Provides a modified version of the original video asset.
- [PHAssetResourceType.adjustmentData](./adjustmentdata.md)
  Provides data for use in reconstructing recent edits to its asset.
- [PHAssetResourceType.pairedVideo](./pairedvideo.md)
  Provides the original video data component of a Live Photo asset.
- [PHAssetResourceType.fullSizePairedVideo](./fullsizepairedvideo.md)
  Provides the current video data component of a Live Photo asset.
- [PHAssetResourceType.adjustmentBaseVideo](./adjustmentbasevideo.md)
  Provides an unaltered version of its video asset.
- [PHAssetResourceType.adjustmentBasePairedVideo](./adjustmentbasepairedvideo.md)
  Provides an unaltered version of the video data for a Live Photo asset for use in reconstructing recent edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcetype/adjustmentbasephoto)*