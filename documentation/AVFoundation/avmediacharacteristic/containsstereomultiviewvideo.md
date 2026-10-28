# containsStereoMultiviewVideo

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static let containsStereoMultiviewVideo: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicContainsStereoMultiviewVideo;
```

## Discussion

Stereoscopic video contains two views with one view for the left eye and one view for the right eye. Multiview video contains more than one view (not necessarily stereoscopic) in the same compressed video sample. The combination of stereoscopic and multiview indicates that multiview carriage is used to carry at least two stereoscopic views. It does not imply that there might not be more than two views. Access to the two stereo views may require opt-in to retrieve both views. Accessing only one of the left or right stereoscopic views as a fallback for playback or compositing where stereoscopic rendering is not supported may itself not be supported.

The value of this characteristic is `public.contains-stereo-multiview-video`.

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
- [static let carriesVideoStereoMetadata: AVMediaCharacteristic](./carriesvideostereometadata.md)
  A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [static let indicatesHorizontalFieldOfView: AVMediaCharacteristic](./indicateshorizontalfieldofview.md)
  A media characteristic that indicates the video track carries information related to the horizontal field of view.
- [static let indicatesNonRectilinearProjection: AVMediaCharacteristic](./indicatesnonrectilinearprojection.md)
  A media characteristic that indicates the video track carries information related to how it should be projected for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/containsstereomultiviewvideo)*