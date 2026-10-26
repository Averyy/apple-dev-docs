# PHAssetMediaSubtype

**Framework**: Photos  
**Kind**: struct  
**Role**: Structure

Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct PHAssetMediaSubtype
```

```c
enum PHAssetMediaSubtype : NSUInteger;
```

#### Overview

You use these constants with the [`PHAsset`](./phasset.md) and [`PHContentEditingInput`](./phcontenteditinginput.md) classes to fetch specific types of assets or to identify an asset being edited.

Media subtypes are [`OptionSet`](../Swift/optionset.md) values, so you can combine them using set literal syntax to test for multiple subtypes.

## Topics

### Initializers
- [init(rawValue: UInt)](./phassetmediasubtype/init%28rawvalue%29.md)
  Initializes a media subtype from a raw value.
### Media Subtypes
- [static var photoPanorama: PHAssetMediaSubtype](./phassetmediasubtype/photopanorama.md)
  The asset is a large-format panorama photo.
- [static var photoHDR: PHAssetMediaSubtype](./phassetmediasubtype/photohdr.md)
  The asset is a high-dynamic range photo.
- [static var photoScreenshot: PHAssetMediaSubtype](./phassetmediasubtype/photoscreenshot.md)
  The asset is an image captured with the device’s screenshot feature.
- [static var photoLive: PHAssetMediaSubtype](./phassetmediasubtype/photolive.md)
  The asset is a Live Photo that includes movement and sounds from the moments just before and after its capture.
- [static var videoCinematic: PHAssetMediaSubtype](./phassetmediasubtype/videocinematic.md)
  The asset is a cinematic video.
- [static var videoStreamed: PHAssetMediaSubtype](./phassetmediasubtype/videostreamed.md)
  The asset is a video with contents that always stream over a network connection.
- [static var videoHighFrameRate: PHAssetMediaSubtype](./phassetmediasubtype/videohighframerate.md)
  The asset is a high-frame-rate video.
- [static var videoTimelapse: PHAssetMediaSubtype](./phassetmediasubtype/videotimelapse.md)
  The asset is a time-lapse video.
- [static var photoDepthEffect: PHAssetMediaSubtype](./phassetmediasubtype/photodeptheffect.md)
  The asset is a photo captured with the Camera app’s Portrait mode depth effect.
### Type Properties
- [static var photoAnimation: PHAssetMediaSubtype](./phassetmediasubtype/photoanimation.md)
- [static var spatialMedia: PHAssetMediaSubtype](./phassetmediasubtype/spatialmedia.md)
- [static var videoScreenRecording: PHAssetMediaSubtype](./phassetmediasubtype/videoscreenrecording.md)
  The media subtype is a photo animation such as a GIF, animated PNGs, etc.

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
- [var sourceType: PHAssetSourceType](./phasset/sourcetype.md)
  The means by which the asset enters the user’s Photos library.
- [struct PHAssetSourceType](./phassetsourcetype.md)
  The means by which an asset enters the Photos library.
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

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetmediasubtype)*