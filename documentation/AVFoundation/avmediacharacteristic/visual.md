# visual

**Framework**: AVFoundation  
**Kind**: property

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

## Mentions

- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)

#### Discussion

Media types with this characteristic include [`video`](avmediatype/video.md), [`subtitle`](avmediatype/subtitle.md), and [`closedCaption`](avmediatype/closedcaption.md).

## See Also

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
- [static let indicatesHorizontalFieldOfView: AVMediaCharacteristic](avmediacharacteristic/indicateshorizontalfieldofview.md)
  A media characteristic that indicates the video track carries information related to the horizontal field of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/visual)*