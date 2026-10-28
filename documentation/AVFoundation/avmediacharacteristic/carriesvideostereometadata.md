# carriesVideoStereoMetadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```c
extern AVMediaCharacteristic const AVMediaCharacteristicCarriesVideoStereoMetadata;
```

## Discussion

This characteristic doesnindicate whether the encoded video contains stereoscopic views. It instead indicates that it contains additional information that may influence the interpretation of those views and contribute to a better experience.

The value of this characteristic is `com.apple.quicktime.video.stereo-metadata`.

> **Note**:  The presence of this characteristic is strictly inferred from the format description of the associated track.

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
- [static let indicatesHorizontalFieldOfView: AVMediaCharacteristic](./indicateshorizontalfieldofview.md)
  A media characteristic that indicates the video track carries information related to the horizontal field of view.
- [static let indicatesNonRectilinearProjection: AVMediaCharacteristic](./indicatesnonrectilinearprojection.md)
  A media characteristic that indicates the video track carries information related to how it should be projected for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/carriesvideostereometadata)*