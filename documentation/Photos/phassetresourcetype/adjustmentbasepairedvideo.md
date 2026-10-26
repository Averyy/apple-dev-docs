# PHAssetResourceType.adjustmentBasePairedVideo

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Provides an unaltered version of the video data for a Live Photo asset for use in reconstructing recent edits.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case adjustmentBasePairedVideo
```

```c
PHAssetResourceTypeAdjustmentBasePairedVideo
```

#### Discussion

This asset resource type appears when fetching the asset resources associated with a Live Photo asset. This resource type represents the input of the most recent edit (if any), to which you can apply the changes described in a [`PHAdjustmentData`](../phadjustmentdata.md) to reconstruct or alter that edit. The corresponding still image can be found in the [`PHAssetResourceType.adjustmentBasePhoto`](./adjustmentbasephoto.md) resource type.

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
- [PHAssetResourceType.adjustmentBasePhoto](./adjustmentbasephoto.md)
  Provides an unaltered version of its photo asset for use in for use in reconstructing recent edits.
- [PHAssetResourceType.pairedVideo](./pairedvideo.md)
  Provides the original video data component of a Live Photo asset.
- [PHAssetResourceType.fullSizePairedVideo](./fullsizepairedvideo.md)
  Provides the current video data component of a Live Photo asset.
- [PHAssetResourceType.adjustmentBaseVideo](./adjustmentbasevideo.md)
  Provides an unaltered version of its video asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcetype/adjustmentbasepairedvideo)*