# carriesVideoStereoMetadata

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static let carriesVideoStereoMetadata: AVMediaCharacteristic
```

#### Discussion

This characteristic doesnindicate whether the encoded video contains stereoscopic views. It instead indicates that it contains additional information that may influence the interpretation of those views and contribute to a better experience.

The value of this characteristic is `com.apple.quicktime.video.stereo-metadata`.

> **Note**:  The presence of this characteristic is strictly inferred from the format description of the associated track.

 The presence of this characteristic is strictly inferred from the format description of the associated track.

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
- [static let indicatesHorizontalFieldOfView: AVMediaCharacteristic](avmediacharacteristic/indicateshorizontalfieldofview.md)
  A media characteristic that indicates the video track carries information related to the horizontal field of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/carriesvideostereometadata)*