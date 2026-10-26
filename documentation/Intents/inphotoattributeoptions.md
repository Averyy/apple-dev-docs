# INPhotoAttributeOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Constants indicating attributes of a photo.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
struct INPhotoAttributeOptions
```

```c
enum INPhotoAttributeOptions : NSUInteger;
```

## Topics

### Photo
- [static var photo: INPhotoAttributeOptions](./inphotoattributeoptions/photo.md)
  A still image.
- [static var bouncePhoto: INPhotoAttributeOptions](./inphotoattributeoptions/bouncephoto.md)
  A live photo edited with the bounce effect.
- [static var burstPhoto: INPhotoAttributeOptions](./inphotoattributeoptions/burstphoto.md)
  A burst-mode photo.
- [static var hdrPhoto: INPhotoAttributeOptions](./inphotoattributeoptions/hdrphoto.md)
  An HDR photo.
- [static var livePhoto: INPhotoAttributeOptions](./inphotoattributeoptions/livephoto.md)
  A live photo.
- [static var longExposurePhoto: INPhotoAttributeOptions](./inphotoattributeoptions/longexposurephoto.md)
  A live photo edited with the long exxposure effect.
- [static var loopPhoto: INPhotoAttributeOptions](./inphotoattributeoptions/loopphoto.md)
  A live photo edited with the loop effect.
- [static var squarePhoto: INPhotoAttributeOptions](./inphotoattributeoptions/squarephoto.md)
  A square photo.
- [static var panoramaPhoto: INPhotoAttributeOptions](./inphotoattributeoptions/panoramaphoto.md)
  A panorama photo.
- [static var portraitPhoto: INPhotoAttributeOptions](./inphotoattributeoptions/portraitphoto.md)
  A portrait photo.
- [static var GIF: INPhotoAttributeOptions](./inphotoattributeoptions/gif.md)
  A Graphics Interchange Format image.
- [static var flash: INPhotoAttributeOptions](./inphotoattributeoptions/flash.md)
  A photo taken with a flash.
- [static var selfie: INPhotoAttributeOptions](./inphotoattributeoptions/selfie.md)
  A selfie.
### Video
- [static var video: INPhotoAttributeOptions](./inphotoattributeoptions/video.md)
  A video.
- [static var timeLapseVideo: INPhotoAttributeOptions](./inphotoattributeoptions/timelapsevideo.md)
  A time-lapse video.
- [static var slowMotionVideo: INPhotoAttributeOptions](./inphotoattributeoptions/slowmotionvideo.md)
  A slow-motion video.
### Filter
- [static var noirFilter: INPhotoAttributeOptions](./inphotoattributeoptions/noirfilter.md)
  A noir filter.
- [static var chromeFilter: INPhotoAttributeOptions](./inphotoattributeoptions/chromefilter.md)
  A chrome filter.
- [static var instantFilter: INPhotoAttributeOptions](./inphotoattributeoptions/instantfilter.md)
  An instant filter.
- [static var tonalFilter: INPhotoAttributeOptions](./inphotoattributeoptions/tonalfilter.md)
  A tonal filter.
- [static var transferFilter: INPhotoAttributeOptions](./inphotoattributeoptions/transferfilter.md)
  A transfer filter.
- [static var monoFilter: INPhotoAttributeOptions](./inphotoattributeoptions/monofilter.md)
  A mono filter.
- [static var fadeFilter: INPhotoAttributeOptions](./inphotoattributeoptions/fadefilter.md)
  A fade filter.
- [static var processFilter: INPhotoAttributeOptions](./inphotoattributeoptions/processfilter.md)
  A process filter.
### Orientation
- [static var landscapeOrientation: INPhotoAttributeOptions](./inphotoattributeoptions/landscapeorientation.md)
  A landscape aspect ratio.
- [static var portraitOrientation: INPhotoAttributeOptions](./inphotoattributeoptions/portraitorientation.md)
  A portrait aspect ratio.
### Other
- [static var favorite: INPhotoAttributeOptions](./inphotoattributeoptions/favorite.md)
  A favorite item.
- [static var frontFacingCamera: INPhotoAttributeOptions](./inphotoattributeoptions/frontfacingcamera.md)
  Taken using a front-facing camera.
- [static var screenshot: INPhotoAttributeOptions](./inphotoattributeoptions/screenshot.md)
  A screenshot.
### Initializers
- [init(rawValue: UInt)](./inphotoattributeoptions/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inphotoattributeoptions)*