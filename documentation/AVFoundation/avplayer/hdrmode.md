# AVPlayer.HDRMode

**Framework**: AVFoundation  
**Kind**: struct

A bitfield type that specifies an HDR mode.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- tvOS 11.2+
- visionOS 1.0+

## Declaration

```swift
struct HDRMode
```

#### Overview

These modes define the available HDR modes. Query [`availableHDRModes`](avplayer/availablehdrmodes.md) to find the HDR modes available for a device.

## Topics

### HDR Modes
- [static var hlg: AVPlayer.HDRMode](avplayer/hdrmode/hlg.md)
  The Hybrid Log-Gamma HDR mode is available.
- [static var hdr10: AVPlayer.HDRMode](avplayer/hdrmode/hdr10.md)
  The HDR10 HDR mode is available.
- [static var dolbyVision: AVPlayer.HDRMode](avplayer/hdrmode/dolbyvision.md)
  The Dolby Vision HDR mode is available.
### Initializers
- [init(rawValue: Int)](avplayer/hdrmode/init(rawvalue:).md)
  Creates an HDR mode with a string value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class var eligibleForHDRPlayback: Bool](avplayer/eligibleforhdrplayback.md)
  A Boolean value that indicates whether the current device can present content to an HDR display.
- [class var availableHDRModes: AVPlayer.HDRMode](avplayer/availablehdrmodes.md)
  The HDR modes that are available for playback.
- [class let eligibleForHDRPlaybackDidChangeNotification: NSNotification.Name](avplayer/eligibleforhdrplaybackdidchangenotification.md)
  A notification that’s posted whenever HDR playback eligibility changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/hdrmode)*