# availableHDRModes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The HDR modes that are available for playback.

**Availability**:
- iOS 11.2+ - Deprecated in 26.0
- iPadOS 11.2+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 11.2+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use eligibleForHDRPlayback instead

## Declaration

```swift
nonisolated
class var availableHDRModes: AVPlayer.HDRMode { get }
```

```objc
@property (class, readonly) AVPlayerHDRMode availableHDRModes;
```

#### Discussion

This property indicates all of the HDR modes that the device can play. A value of `0` indicates the device doesn’t support HDR. Each value indicates that an appropriate HDR display is available for the specified HDR mode. Additionally, the device must be capable of playing the specified HDR type.

This property doesn’t indicate whether a video contains HDR content, HDR video is currently playing, or if video is playing on an HDR display.

> ❗ **Important**:  Mac apps built with Mac Catalyst don’t support HDR playback on Intel-based Mac computers. When playing HDR content over HTTP Live Streaming, [`AVPlayer`](../avplayer.md) selects the SDR variant playlist. When playing file-based media, HDR content is tone mapped to SDR before it’s rendered onscreen.

## See Also

### Determining HDR playback eligibility
- [class var eligibleForHDRPlayback: Bool](./eligibleforhdrplayback.md)
  A Boolean value that indicates whether the current device can present content to an HDR display.
- [AVPlayer.HDRMode](./hdrmode.md)
  A bitfield type that specifies an HDR mode.
- [class let eligibleForHDRPlaybackDidChangeNotification: NSNotification.Name](./eligibleforhdrplaybackdidchangenotification.md)
  A notification that’s posted whenever HDR playback eligibility changes.
- [AVPlayerAvailableHDRModesDidChangeNotification](../avplayeravailablehdrmodesdidchangenotification.md)
  A notification that fires whenever availableHDRModes changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/availablehdrmodes)*