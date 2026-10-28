# usesWideGamutColorSpace

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates that a track uses a wide-gamut color space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let usesWideGamutColorSpace: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicUsesWideGamutColorSpace;
```

## Mentions

- [Tagging media with video color information](../tagging-media-with-video-color-information.md)

## Discussion

Tracks that use a wide-gamut color space may use colors that can’t be accurately represented in standard RGB mode.

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
- [static let containsStereoMultiviewVideo: AVMediaCharacteristic](./containsstereomultiviewvideo.md)
  A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [static let carriesVideoStereoMetadata: AVMediaCharacteristic](./carriesvideostereometadata.md)
  A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [static let indicatesHorizontalFieldOfView: AVMediaCharacteristic](./indicateshorizontalfieldofview.md)
  A media characteristic that indicates the video track carries information related to the horizontal field of view.
- [static let indicatesNonRectilinearProjection: AVMediaCharacteristic](./indicatesnonrectilinearprojection.md)
  A media characteristic that indicates the video track carries information related to how it should be projected for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/useswidegamutcolorspace)*