# containsHDRVideo

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates that a track contains HDR video.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let containsHDRVideo: AVMediaCharacteristic
```

#### Discussion

HDR video contains extended dynamic range that requires explicit support when compositing. The system infers this characteristic from the format description of the associated track.

The value of this characteristic is `public.contains-hdr-video`.

## See Also

- [static let visual: AVMediaCharacteristic](avmediacharacteristic/visual.md)
  A media characteristic that indicates that a track or media selection option includes visual content.
- [static let containsAlphaChannel: AVMediaCharacteristic](avmediacharacteristic/containsalphachannel.md)
  A media characteristic that indicates that a track contains an alpha channel.
- [static let frameBased: AVMediaCharacteristic](avmediacharacteristic/framebased.md)
  A media characteristic that indicates that a track or media selection option includes frame-based content.
- [static let usesWideGamutColorSpace: AVMediaCharacteristic](avmediacharacteristic/useswidegamutcolorspace.md)
  A media characteristic that indicates that a track uses a wide-gamut color space.
- [static let containsStereoMultiviewVideo: AVMediaCharacteristic](avmediacharacteristic/containsstereomultiviewvideo.md)
  A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [static let carriesVideoStereoMetadata: AVMediaCharacteristic](avmediacharacteristic/carriesvideostereometadata.md)
  A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [static let indicatesHorizontalFieldOfView: AVMediaCharacteristic](avmediacharacteristic/indicateshorizontalfieldofview.md)
  A media characteristic that indicates the video track carries information related to the horizontal field of view.
- [static let indicatesNonRectilinearProjection: AVMediaCharacteristic](avmediacharacteristic/indicatesnonrectilinearprojection.md)
  A media characteristic that indicates the video track carries information related to how it should be projected for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/containshdrvideo)*