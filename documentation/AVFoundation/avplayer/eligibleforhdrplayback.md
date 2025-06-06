# eligibleForHDRPlayback

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the current device can present content to an HDR display.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class var eligibleForHDRPlayback: Bool { get }
```

#### Discussion

This property is not key-value observable.

## See Also

- [class var availableHDRModes: AVPlayer.HDRMode](avplayer/availablehdrmodes.md)
  The HDR modes that are available for playback.
- [AVPlayer.HDRMode](avplayer/hdrmode.md)
  A bitfield type that specifies an HDR mode.
- [class let eligibleForHDRPlaybackDidChangeNotification: NSNotification.Name](avplayer/eligibleforhdrplaybackdidchangenotification.md)
  A notification that’s posted whenever HDR playback eligibility changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/eligibleforhdrplayback)*