# performEffect(for:)

**Framework**: AVFoundation  
**Kind**: method

Performs the specified reaction type on the video stream.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func performEffect(for reactionType: AVCaptureReactionType)
```

#### Discussion

The entries in the [`reactionEffectsInProgress`](avcapturedevice/reactioneffectsinprogress.md) property may not reflect one-to-one with calls to this method. Depending on reaction style or resource limits, the system may coalesce overlapping reactions of the same type by extending an existing reaction rather than overlaying a new one.

> **Note**:  Calling this method has no effect when the value of [`canPerformReactionEffects`](avcapturedevice/canperformreactioneffects.md) is [`false`](https://developer.apple.com/documentation/Swift/false). In this case, VoIP apps should transmit and display reactions outside of the video feed.

## Parameters

- `reactionType`: A reaction type to perform. Specifying a type that doesn’t exists within the set of   for the device results in an exception.

## See Also

- [class var reactionEffectsEnabled: Bool](avcapturedevice/reactioneffectsenabled.md)
  A Boolean value that indicates whether the app supports performing reaction effects.
- [var canPerformReactionEffects: Bool](avcapturedevice/canperformreactioneffects.md)
  A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [var availableReactionTypes: Set<AVCaptureReactionType>](avcapturedevice/availablereactiontypes.md)
  A set of reactions types that a device supports performing.
- [class var reactionEffectGesturesEnabled: Bool](avcapturedevice/reactioneffectgesturesenabled.md)
  A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [var reactionEffectsInProgress: [AVCaptureReactionEffectState]](avcapturedevice/reactioneffectsinprogress.md)
  An array of reaction effects that the device is currently performing, sorted by timestamp.
- [class AVCaptureReactionEffectState](avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/performeffect(for:))*