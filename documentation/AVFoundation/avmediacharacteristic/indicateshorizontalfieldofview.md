# indicatesHorizontalFieldOfView

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates the video track carries information related to the horizontal field of view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static let indicatesHorizontalFieldOfView: AVMediaCharacteristic
```

#### Discussion

This media characteristic is present when the [`CMVideoFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMVideoFormatDescription) includes a [`kCMFormatDescriptionExtension_HorizontalFieldOfView`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionExtension_HorizontalFieldOfView) extension. This is not an indication that the field of view is expanded beyond or more narrow than typical horizontal fields of view.

The value of this characteristic is `public.indicates-horizontal-field-of-view`.

> **Note**:  The presence of this characteristic is strictly inferred from the format description of the associated track.

## See Also

- [static let visual: AVMediaCharacteristic](avmediacharacteristic/visual.md)
  A media characteristic that indicates that a track or media selection option includes visual content.
- [static let containsAlphaChannel: AVMediaCharacteristic](avmediacharacteristic/containsalphachannel.md)
  A media characteristic that indicates that a track contains an alpha channel.
- [static let containsHDRVideo: AVMediaCharacteristic](avmediacharacteristic/containshdrvideo.md)
  A media characteristic that indicates that a track contains HDR video.
- [static let frameBased: AVMediaCharacteristic](avmediacharacteristic/framebased.md)
  A media characteristic that indicates that a track or media selection option includes frame-based content.
- [static let usesWideGamutColorSpace: AVMediaCharacteristic](avmediacharacteristic/useswidegamutcolorspace.md)
  A media characteristic that indicates that a track uses a wide-gamut color space.
- [static let containsStereoMultiviewVideo: AVMediaCharacteristic](avmediacharacteristic/containsstereomultiviewvideo.md)
  A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [static let carriesVideoStereoMetadata: AVMediaCharacteristic](avmediacharacteristic/carriesvideostereometadata.md)
  A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [static let indicatesNonRectilinearProjection: AVMediaCharacteristic](avmediacharacteristic/indicatesnonrectilinearprojection.md)
  A media characteristic that indicates the video track carries information related to how it should be projected for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/indicateshorizontalfieldofview)*