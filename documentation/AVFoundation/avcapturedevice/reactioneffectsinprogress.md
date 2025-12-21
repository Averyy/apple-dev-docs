# reactionEffectsInProgress

**Framework**: AVFoundation  
**Kind**: property

An array of reaction effects that the device is currently performing, sorted by timestamp.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var reactionEffectsInProgress: [AVCaptureReactionEffectState] { get }
```

#### Discussion

Key-value observe this property to determine when reaction effects begin and end. If your key-value observing callback provides old and new values, any in-progress reaction effects in the new array have a value of [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid) for their [`endTime`](avcapturereactioneffectstate/endtime.md) property value. Completed reaction effects are only in the old array, and have their [`endTime`](avcapturereactioneffectstate/endtime.md) property value set to the presentation time of the first frame where the reaction effect was no longer present.

## See Also

- [class var reactionEffectsEnabled: Bool](avcapturedevice/reactioneffectsenabled.md)
  A Boolean value that indicates whether the app supports performing reaction effects.
- [var canPerformReactionEffects: Bool](avcapturedevice/canperformreactioneffects.md)
  A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [var availableReactionTypes: Set<AVCaptureReactionType>](avcapturedevice/availablereactiontypes.md)
  A set of reactions types that a device supports performing.
- [class var reactionEffectGesturesEnabled: Bool](avcapturedevice/reactioneffectgesturesenabled.md)
  A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [func performEffect(for: AVCaptureReactionType)](avcapturedevice/performeffect(for:).md)
  Performs the specified reaction type on the video stream.
- [class AVCaptureReactionEffectState](avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/reactioneffectsinprogress)*