# photoLive

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

The asset is a Live Photo that includes movement and sounds from the moments just before and after its capture.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var photoLive: PHAssetMediaSubtype { get }
```

```c
PHAssetMediaSubtypePhotoLive
```

#### Discussion

To display a Live Photo asset with its associated video content, retrieve a [`PHLivePhoto`](../phlivephoto.md) object using the [`PHImageManager`](../phimagemanager.md) class and assign it to a [`PHLivePhotoView`](https://developer.apple.com/documentation/photosui/phlivephotoview) object.

## See Also

### Media Subtypes
- [static var photoPanorama: PHAssetMediaSubtype](./photopanorama.md)
  The asset is a large-format panorama photo.
- [static var photoHDR: PHAssetMediaSubtype](./photohdr.md)
  The asset is a high-dynamic range photo.
- [static var photoScreenshot: PHAssetMediaSubtype](./photoscreenshot.md)
  The asset is an image captured with the device’s screenshot feature.
- [static var videoCinematic: PHAssetMediaSubtype](./videocinematic.md)
  The asset is a cinematic video.
- [static var videoStreamed: PHAssetMediaSubtype](./videostreamed.md)
  The asset is a video with contents that always stream over a network connection.
- [static var videoHighFrameRate: PHAssetMediaSubtype](./videohighframerate.md)
  The asset is a high-frame-rate video.
- [static var videoTimelapse: PHAssetMediaSubtype](./videotimelapse.md)
  The asset is a time-lapse video.
- [static var photoDepthEffect: PHAssetMediaSubtype](./photodeptheffect.md)
  The asset is a photo captured with the Camera app’s Portrait mode depth effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetmediasubtype/photolive)*