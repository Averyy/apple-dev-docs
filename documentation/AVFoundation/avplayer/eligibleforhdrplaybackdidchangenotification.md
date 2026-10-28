# eligibleForHDRPlaybackDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification that’s posted whenever HDR playback eligibility changes.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
class let eligibleForHDRPlaybackDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVPlayerEligibleForHDRPlaybackDidChangeNotification;
```

## Discussion

The system may post this notification if a user connects or disconnects a display, or makes other system resource changes.

## See Also

### Determining HDR playback eligibility
- [class var eligibleForHDRPlayback: Bool](./eligibleforhdrplayback.md)
  A Boolean value that indicates whether the current device can present content to an HDR display.
- [class var availableHDRModes: AVPlayer.HDRMode](./availablehdrmodes.md)
  The HDR modes that are available for playback.
- [AVPlayer.HDRMode](./hdrmode.md)
  A bitfield type that specifies an HDR mode.
- [AVPlayerAvailableHDRModesDidChangeNotification](../avplayeravailablehdrmodesdidchangenotification.md)
  A notification that fires whenever availableHDRModes changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/eligibleforhdrplaybackdidchangenotification)*