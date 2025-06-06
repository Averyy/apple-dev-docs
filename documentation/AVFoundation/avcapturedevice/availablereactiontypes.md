# availableReactionTypes

**Framework**: AVFoundation  
**Kind**: property

A set of reactions types that a device supports performing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var availableReactionTypes: Set<AVCaptureReactionType> { get }
```

#### Discussion

The list may differ between devices, and may change for a specific device when it’s active format changes.

This property is key-value observable.

## See Also

- [class var reactionEffectsEnabled: Bool](avcapturedevice/reactioneffectsenabled.md)
  A Boolean value that indicates whether the app supports performing reaction effects.
- [var canPerformReactionEffects: Bool](avcapturedevice/canperformreactioneffects.md)
  A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [class var reactionEffectGesturesEnabled: Bool](avcapturedevice/reactioneffectgesturesenabled.md)
  A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [func performEffect(for: AVCaptureReactionType)](avcapturedevice/performeffect(for:).md)
  Performs the specified reaction type on the video stream.
- [var reactionEffectsInProgress: [AVCaptureReactionEffectState]](avcapturedevice/reactioneffectsinprogress.md)
  An array of reaction effects that the device is currently performing, sorted by timestamp.
- [class AVCaptureReactionEffectState](avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/availablereactiontypes)*