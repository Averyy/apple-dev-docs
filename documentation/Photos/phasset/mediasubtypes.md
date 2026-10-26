# mediaSubtypes

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The subtypes of the asset, identifying special kinds of assets, such as panoramic photo or high-frame-rate video.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var mediaSubtypes: PHAssetMediaSubtype { get }
```

```objc
@property (nonatomic, assign, readonly) PHAssetMediaSubtype mediaSubtypes;
```

#### Discussion

See [`PHAssetMediaSubtype`](../phassetmediasubtype.md) for possible values.

Because an asset may have more than one subtype, you use these values as bit masks to identify an asset. For example, the code below tests an asset for the panorama photo subtype:

```objc
if (asset.mediaType == PHAssetMediaTypeImage && (asset.mediaSubtypes & PHAssetMediaSubtypePhotoHDR)) {
    // display HDR badge in UI
}
```

## See Also

### Reading Asset Metadata
- [var contentType: UTType](./contenttype.md)
  The type of image or video data that is presented for the asset
- [var mediaType: PHAssetMediaType](./mediatype.md)
  The type of the asset, such as video or audio.
- [enum PHAssetMediaType](../phassetmediatype.md)
  Identifies the general type of an asset, such as image or video.
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
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that indicates whether the user hides the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/mediasubtypes)*