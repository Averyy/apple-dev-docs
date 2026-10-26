# PHAssetCollectionSubtype

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Minor distinctions between kinds of asset collections, used by the [`assetCollectionSubtype`](./phassetcollection/assetcollectionsubtype.md) property and the [`fetchAssetCollections(with:subtype:options:)`](./phassetcollection/fetchassetcollections%28with,subtype,options%29.md) method.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHAssetCollectionSubtype
```

```c
enum PHAssetCollectionSubtype : NSInteger;
```

## Topics

### User Album Types
- [PHAssetCollectionSubtype.albumRegular](./phassetcollectionsubtype/albumregular.md)
  An album created in the Photos app.
- [PHAssetCollectionSubtype.albumSyncedEvent](./phassetcollectionsubtype/albumsyncedevent.md)
  An Event synced to the device from a Mac.
- [PHAssetCollectionSubtype.albumSyncedFaces](./phassetcollectionsubtype/albumsyncedfaces.md)
  A Faces group synced to the device from a Mac.
- [PHAssetCollectionSubtype.albumSyncedAlbum](./phassetcollectionsubtype/albumsyncedalbum.md)
  An album synced to the device from a Mac.
- [PHAssetCollectionSubtype.albumImported](./phassetcollectionsubtype/albumimported.md)
  An album imported from a camera or external storage.
### Cloud Album Types
- [PHAssetCollectionSubtype.albumMyPhotoStream](./phassetcollectionsubtype/albummyphotostream.md)
  The user’s personal iCloud Photo Stream.
- [PHAssetCollectionSubtype.albumCloudShared](./phassetcollectionsubtype/albumcloudshared.md)
  An iCloud Shared Photo Stream.
### Smart Album Types
- [PHAssetCollectionSubtype.smartAlbumAllHidden](./phassetcollectionsubtype/smartalbumallhidden.md)
  A Smart Album that groups all assets hidden from the Moments view in the Photos app.
- [PHAssetCollectionSubtype.smartAlbumAnimated](./phassetcollectionsubtype/smartalbumanimated.md)
  A Smart Album that groups all image animation assets.
- [PHAssetCollectionSubtype.smartAlbumBursts](./phassetcollectionsubtype/smartalbumbursts.md)
  A Smart Album that groups all burst photo sequences in the photo library.
- [PHAssetCollectionSubtype.smartAlbumCinematic](./phassetcollectionsubtype/smartalbumcinematic.md)
  A Smart Album that groups all cinematic photo assets.
- [PHAssetCollectionSubtype.smartAlbumDepthEffect](./phassetcollectionsubtype/smartalbumdeptheffect.md)
  A Smart Album that groups all images captured using the Depth Effect camera mode on compatible devices.
- [PHAssetCollectionSubtype.smartAlbumFavorites](./phassetcollectionsubtype/smartalbumfavorites.md)
  A Smart Album that groups all assets that the user marks as favorites.
- [PHAssetCollectionSubtype.smartAlbumGeneric](./phassetcollectionsubtype/smartalbumgeneric.md)
  A Smart Album without a more-specific subtype.
- [PHAssetCollectionSubtype.smartAlbumLivePhotos](./phassetcollectionsubtype/smartalbumlivephotos.md)
  A Smart Album that groups all Live Photos assets.
- [PHAssetCollectionSubtype.smartAlbumLongExposures](./phassetcollectionsubtype/smartalbumlongexposures.md)
  A Smart Album that groups all Live Photos assets where the Long Exposure variation is in an enabled state.
- [PHAssetCollectionSubtype.smartAlbumPanoramas](./phassetcollectionsubtype/smartalbumpanoramas.md)
  A Smart Album that groups all panorama photos in the photo library.
- [PHAssetCollectionSubtype.smartAlbumRAW](./phassetcollectionsubtype/smartalbumraw.md)
  A Smart Album that groups all RAW assets in the photo library.
- [PHAssetCollectionSubtype.smartAlbumRecentlyAdded](./phassetcollectionsubtype/smartalbumrecentlyadded.md)
  A Smart Album that groups all recently added assets in the photo library.
- [PHAssetCollectionSubtype.smartAlbumScreenshots](./phassetcollectionsubtype/smartalbumscreenshots.md)
  A Smart Album that groups all images captured using the device’s screenshot function.
- [PHAssetCollectionSubtype.smartAlbumSelfPortraits](./phassetcollectionsubtype/smartalbumselfportraits.md)
  A Smart Album that groups all photos and videos captured using the device’s front-facing camera.
- [PHAssetCollectionSubtype.smartAlbumSlomoVideos](./phassetcollectionsubtype/smartalbumslomovideos.md)
  A Smart Album that groups all Slow-Mo videos in the photo library.
- [PHAssetCollectionSubtype.smartAlbumScreenRecordings](./phassetcollectionsubtype/smartalbumscreenrecordings.md)
  A Smart Album that groups all videos captured using the device’s screenrecordings function.
- [PHAssetCollectionSubtype.smartAlbumSpatial](./phassetcollectionsubtype/smartalbumspatial.md)
- [PHAssetCollectionSubtype.smartAlbumTimelapses](./phassetcollectionsubtype/smartalbumtimelapses.md)
  A Smart Album that groups all time-lapse videos in the photo library.
- [PHAssetCollectionSubtype.smartAlbumUnableToUpload](./phassetcollectionsubtype/smartalbumunabletoupload.md)
  A Smart Album that groups all assets that the system can’t upload to iCloud.
- [PHAssetCollectionSubtype.smartAlbumUserLibrary](./phassetcollectionsubtype/smartalbumuserlibrary.md)
  A Smart Album that groups all assets that originate in the user’s own library (as opposed to assets from iCloud Shared Albums).
- [PHAssetCollectionSubtype.smartAlbumVideos](./phassetcollectionsubtype/smartalbumvideos.md)
  A Smart Album that groups all video assets in the photo library.
### Wildcard Search
- [PHAssetCollectionSubtype.any](./phassetcollectionsubtype/any.md)
  A bit mask representing all possible subtypes.
### Initializers
- [init?(rawValue: Int)](./phassetcollectionsubtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reading Asset Collection Metadata
- [var assetCollectionType: PHAssetCollectionType](./phassetcollection/assetcollectiontype.md)
  The type of the asset collection, such as an album or a moment.
- [enum PHAssetCollectionType](./phassetcollectiontype.md)
  Major distinctions between kinds of asset collections, used by the [`assetCollectionType`](./phassetcollection/assetcollectiontype.md) property and the [`fetchAssetCollectionsContaining(_:with:options:)`](./phassetcollection/fetchassetcollectionscontaining%28_,with,options%29.md) and [`fetchAssetCollections(with:subtype:options:)`](./phassetcollection/fetchassetcollections%28with,subtype,options%29.md) methods.
- [var assetCollectionSubtype: PHAssetCollectionSubtype](./phassetcollection/assetcollectionsubtype.md)
  The subtype of the asset collection.
- [var estimatedAssetCount: Int](./phassetcollection/estimatedassetcount.md)
  The estimated number of assets in the asset collection.
- [var startDate: Date?](./phassetcollection/startdate.md)
  The earliest creation date among all assets in the asset collection.
- [var endDate: Date?](./phassetcollection/enddate.md)
  The latest creation date among all assets in the asset collection.
- [var approximateLocation: CLLocation?](./phassetcollection/approximatelocation.md)
  A location representing those of all assets in the collection.
- [var localizedLocationNames: [String]](./phassetcollection/localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionsubtype)*