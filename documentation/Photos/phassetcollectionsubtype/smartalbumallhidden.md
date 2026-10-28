# PHAssetCollectionSubtype.smartAlbumAllHidden

**Framework**: Photos  
**Kind**: case  
**Role**: Case

A Smart Album that groups all assets hidden from the Moments view in the Photos app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case smartAlbumAllHidden
```

```c
PHAssetCollectionSubtypeSmartAlbumAllHidden
```

## Discussion

Hidden assets have an [`isHidden`](../phasset/ishidden.md) value of `true` and the system doesn’t return them through a fetch request, by default. Hide or show an asset by setting the [`isHidden`](../phassetchangerequest/ishidden.md) property of a [`PHAssetChangeRequest`](../phassetchangerequest.md) object.

Beginning with iOS 16, users can require authentication to view the hidden Smart Album, and the user setting is `true` by default. When `true`, the system returns an empty Smart Album.

## See Also

### Smart Album Types
- [PHAssetCollectionSubtype.smartAlbumAnimated](./smartalbumanimated.md)
  A Smart Album that groups all image animation assets.
- [PHAssetCollectionSubtype.smartAlbumBursts](./smartalbumbursts.md)
  A Smart Album that groups all burst photo sequences in the photo library.
- [PHAssetCollectionSubtype.smartAlbumCinematic](./smartalbumcinematic.md)
  A Smart Album that groups all cinematic photo assets.
- [PHAssetCollectionSubtype.smartAlbumDepthEffect](./smartalbumdeptheffect.md)
  A Smart Album that groups all images captured using the Depth Effect camera mode on compatible devices.
- [PHAssetCollectionSubtype.smartAlbumFavorites](./smartalbumfavorites.md)
  A Smart Album that groups all assets that the user marks as favorites.
- [PHAssetCollectionSubtype.smartAlbumGeneric](./smartalbumgeneric.md)
  A Smart Album without a more-specific subtype.
- [PHAssetCollectionSubtype.smartAlbumLivePhotos](./smartalbumlivephotos.md)
  A Smart Album that groups all Live Photos assets.
- [PHAssetCollectionSubtype.smartAlbumLongExposures](./smartalbumlongexposures.md)
  A Smart Album that groups all Live Photos assets where the Long Exposure variation is in an enabled state.
- [PHAssetCollectionSubtype.smartAlbumPanoramas](./smartalbumpanoramas.md)
  A Smart Album that groups all panorama photos in the photo library.
- [PHAssetCollectionSubtype.smartAlbumRAW](./smartalbumraw.md)
  A Smart Album that groups all RAW assets in the photo library.
- [PHAssetCollectionSubtype.smartAlbumRecentlyAdded](./smartalbumrecentlyadded.md)
  A Smart Album that groups all recently added assets in the photo library.
- [PHAssetCollectionSubtype.smartAlbumScreenshots](./smartalbumscreenshots.md)
  A Smart Album that groups all images captured using the device’s screenshot function.
- [PHAssetCollectionSubtype.smartAlbumSelfPortraits](./smartalbumselfportraits.md)
  A Smart Album that groups all photos and videos captured using the device’s front-facing camera.
- [PHAssetCollectionSubtype.smartAlbumSlomoVideos](./smartalbumslomovideos.md)
  A Smart Album that groups all Slow-Mo videos in the photo library.
- [PHAssetCollectionSubtype.smartAlbumScreenRecordings](./smartalbumscreenrecordings.md)
  A Smart Album that groups all videos captured using the device’s screenrecordings function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionsubtype/smartalbumallhidden)*