# PHAsset.Rating

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

A rating for an asset, from unset (no rating chosen) up to five stars.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Rating
```

```c
enum PHAssetRating : NSInteger;
```

## Topics

### Ratings
- [PHAsset.Rating.unset](./rating-swift.enum/unset.md)
- [PHAsset.Rating.one](./rating-swift.enum/one.md)
- [PHAsset.Rating.two](./rating-swift.enum/two.md)
- [PHAsset.Rating.three](./rating-swift.enum/three.md)
- [PHAsset.Rating.four](./rating-swift.enum/four.md)
- [PHAsset.Rating.five](./rating-swift.enum/five.md)
### Initializers
- [init?(rawValue: Int)](./rating-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading Asset Metadata
- [var contentType: UTType](./contenttype.md)
  The type of image or video data that is presented for the asset
- [var mediaType: PHAssetMediaType](./mediatype.md)
  The type of the asset, such as video or audio.
- [enum PHAssetMediaType](../phassetmediatype.md)
  Identifies the general type of an asset, such as image or video.
- [var mediaSubtypes: PHAssetMediaSubtype](./mediasubtypes.md)
  The subtypes of the asset, identifying special kinds of assets, such as panoramic photo or high-frame-rate video.
- [struct PHAssetMediaSubtype](../phassetmediasubtype.md)
  Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [var sourceType: PHAssetSourceType](./sourcetype.md)
  The means by which the asset enters the user’s Photos library.
- [struct PHAssetSourceType](../phassetsourcetype.md)
  The means by which an asset enters the Photos library.
- [var pixelWidth: Int](./pixelwidth.md)
  The width, in pixels, of the asset’s image or video data.
- [var pixelHeight: Int](./pixelheight.md)
  The height, in pixels, of the asset’s image or video data.
- [var addedDate: Date?](./addeddate.md)
  The date and time this asset was added to the photo library (from the device that was used to add this asset)
- [var creationDate: Date?](./creationdate.md)
  The date and time of the asset’s creation.
- [var modificationDate: Date?](./modificationdate.md)
  The date and time of the asset’s last modification.
- [var location: CLLocation?](./location.md)
  The location information for the asset.
- [var duration: TimeInterval](./duration.md)
  The duration, in seconds, of the video asset.
- [var isFavorite: Bool](./isfavorite.md)
  A Boolean value that indicates whether the user marks the asset as a favorite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/rating-swift.enum)*