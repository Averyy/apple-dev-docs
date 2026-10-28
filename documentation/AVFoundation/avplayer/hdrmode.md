# AVPlayer.HDRMode

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A bitfield type that specifies an HDR mode.

**Availability**:
- iOS 11.2+ - Deprecated in 26.0
- iPadOS 11.2+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 11.2+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: The deprecated availableHDRModes uses this enum. Use eligibleForHDRPlayback instead

## Declaration

```swift
struct HDRMode
```

```c
enum AVPlayerHDRMode : NSInteger;
```

## Overview

These modes define the available HDR modes. Query [`availableHDRModes`](./availablehdrmodes.md) to find the HDR modes available for a device.

## Topics

### HDR modes
- [static var hlg: AVPlayer.HDRMode](./hdrmode/hlg.md)
  The Hybrid Log-Gamma HDR mode is available.
- [static var hdr10: AVPlayer.HDRMode](./hdrmode/hdr10.md)
  The HDR10 HDR mode is available.
- [static var dolbyVision: AVPlayer.HDRMode](./hdrmode/dolbyvision.md)
  The Dolby Vision HDR mode is available.
### Initializers
- [init(rawValue: Int)](./hdrmode/init%28rawvalue%29.md)
  Creates an HDR mode with a string value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Determining HDR playback eligibility
- [class var eligibleForHDRPlayback: Bool](./eligibleforhdrplayback.md)
  A Boolean value that indicates whether the current device can present content to an HDR display.
- [class var availableHDRModes: AVPlayer.HDRMode](./availablehdrmodes.md)
  The HDR modes that are available for playback.
- [class let eligibleForHDRPlaybackDidChangeNotification: NSNotification.Name](./eligibleforhdrplaybackdidchangenotification.md)
  A notification that’s posted whenever HDR playback eligibility changes.
- [AVPlayerAvailableHDRModesDidChangeNotification](../avplayeravailablehdrmodesdidchangenotification.md)
  A notification that fires whenever availableHDRModes changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/hdrmode)*