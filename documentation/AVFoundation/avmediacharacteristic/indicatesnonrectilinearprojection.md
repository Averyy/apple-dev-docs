# indicatesNonRectilinearProjection

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates the video track carries information related to how it should be projected for display.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let indicatesNonRectilinearProjection: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicIndicatesNonRectilinearProjection;
```

#### Discussion

This media characteristic is currently synthesized if the CMVideoFormatDescription specifies a non-rectilinear projection. To determine which kind of projection is indicated, look for the format description extension with key kCMFormatDescriptionExtension_ProjectionKind. The value of this characteristic is @“public.indicates-non-rectilinear-projection”. Note for content authors: the presence of this characteristic is strictly inferred from the format description of the associated track.

## See Also

### Visual
- [static let visual: AVMediaCharacteristic](./visual.md)
  A media characteristic that indicates that a track or media selection option includes visual content.
- [static let containsAlphaChannel: AVMediaCharacteristic](./containsalphachannel.md)
  A media characteristic that indicates that a track contains an alpha channel.
- [static let containsHDRVideo: AVMediaCharacteristic](./containshdrvideo.md)
  A media characteristic that indicates that a track contains HDR video.
- [static let frameBased: AVMediaCharacteristic](./framebased.md)
  A media characteristic that indicates that a track or media selection option includes frame-based content.
- [static let usesWideGamutColorSpace: AVMediaCharacteristic](./useswidegamutcolorspace.md)
  A media characteristic that indicates that a track uses a wide-gamut color space.
- [static let containsStereoMultiviewVideo: AVMediaCharacteristic](./containsstereomultiviewvideo.md)
  A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [static let carriesVideoStereoMetadata: AVMediaCharacteristic](./carriesvideostereometadata.md)
  A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [static let indicatesHorizontalFieldOfView: AVMediaCharacteristic](./indicateshorizontalfieldofview.md)
  A media characteristic that indicates the video track carries information related to the horizontal field of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/indicatesnonrectilinearprojection)*