# PHAssetSourceType

**Framework**: Photos  
**Kind**: struct  
**Role**: Structure

The means by which an asset enters the Photos library.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct PHAssetSourceType
```

```c
enum PHAssetSourceType : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./phassetsourcetype/init%28rawvalue%29.md)
  Initializes an asset source type from a raw value.
### Constants
- [static var typeUserLibrary: PHAssetSourceType](./phassetsourcetype/typeuserlibrary.md)
  The asset is part of the user’s main Photos library.
- [static var typeCloudShared: PHAssetSourceType](./phassetsourcetype/typecloudshared.md)
  The asset originates from an iCloud Shared Album.
- [static var typeiTunesSynced: PHAssetSourceType](./phassetsourcetype/typeitunessynced.md)
  The asset originates from a Mac or PC and is present on the device through iTunes sync.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Reading Asset Metadata
- [var contentType: UTType](./phasset/contenttype.md)
  The type of image or video data that is presented for the asset
- [var mediaType: PHAssetMediaType](./phasset/mediatype.md)
  The type of the asset, such as video or audio.
- [enum PHAssetMediaType](./phassetmediatype.md)
  Identifies the general type of an asset, such as image or video.
- [var mediaSubtypes: PHAssetMediaSubtype](./phasset/mediasubtypes.md)
  The subtypes of the asset, identifying special kinds of assets, such as panoramic photo or high-frame-rate video.
- [struct PHAssetMediaSubtype](./phassetmediasubtype.md)
  Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [var sourceType: PHAssetSourceType](./phasset/sourcetype.md)
  The means by which the asset enters the user’s Photos library.
- [var pixelWidth: Int](./phasset/pixelwidth.md)
  The width, in pixels, of the asset’s image or video data.
- [var pixelHeight: Int](./phasset/pixelheight.md)
  The height, in pixels, of the asset’s image or video data.
- [var addedDate: Date?](./phasset/addeddate.md)
  The date and time this asset was added to the photo library (from the device that was used to add this asset)
- [var creationDate: Date?](./phasset/creationdate.md)
  The date and time of the asset’s creation.
- [var modificationDate: Date?](./phasset/modificationdate.md)
  The date and time of the asset’s last modification.
- [var location: CLLocation?](./phasset/location.md)
  The location information for the asset.
- [var duration: TimeInterval](./phasset/duration.md)
  The duration, in seconds, of the video asset.
- [var isFavorite: Bool](./phasset/isfavorite.md)
  A Boolean value that indicates whether the user marks the asset as a favorite.
- [var isHidden: Bool](./phasset/ishidden.md)
  A Boolean value that indicates whether the user hides the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetsourcetype)*