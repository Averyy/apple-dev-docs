# visual

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates that a track or media selection option includes visual content.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static let visual: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicVisual;
```

## Mentions

- [Selecting subtitles and alternative audio tracks](../selecting-subtitles-and-alternative-audio-tracks.md)

## Discussion

Media types with this characteristic include [`video`](../avmediatype/video.md), [`subtitle`](../avmediatype/subtitle.md), and [`closedCaption`](../avmediatype/closedcaption.md).

## See Also

### Visual
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
- [static let indicatesNonRectilinearProjection: AVMediaCharacteristic](./indicatesnonrectilinearprojection.md)
  A media characteristic that indicates the video track carries information related to how it should be projected for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/visual)*