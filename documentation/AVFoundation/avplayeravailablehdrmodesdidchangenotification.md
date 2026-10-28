# AVPlayerAvailableHDRModesDidChangeNotification

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A notification that fires whenever availableHDRModes changes.

**Availability**:
- iOS 11.2+ - Deprecated in 26.0
- iPadOS 11.2+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 11.2+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```c
extern NSNotificationName const AVPlayerAvailableHDRModesDidChangeNotification;
```

## Discussion

This notification fires when a value is added or removed from the list of availableHDRModes. This can be caused by display connection/disconnection or resource changes.

## See Also

### Determining HDR playback eligibility
- [class var eligibleForHDRPlayback: Bool](./avplayer/eligibleforhdrplayback.md)
  A Boolean value that indicates whether the current device can present content to an HDR display.
- [class var availableHDRModes: AVPlayer.HDRMode](./avplayer/availablehdrmodes.md)
  The HDR modes that are available for playback.
- [AVPlayer.HDRMode](./avplayer/hdrmode.md)
  A bitfield type that specifies an HDR mode.
- [class let eligibleForHDRPlaybackDidChangeNotification: NSNotification.Name](./avplayer/eligibleforhdrplaybackdidchangenotification.md)
  A notification that’s posted whenever HDR playback eligibility changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeravailablehdrmodesdidchangenotification)*