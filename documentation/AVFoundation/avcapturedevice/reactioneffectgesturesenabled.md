# reactionEffectGesturesEnabled

**Framework**: Avfoundation  
**Kind**: property

A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class var reactionEffectGesturesEnabled: Bool { get }
```

#### Discussion

This property reflects the enabled state of Gestures in Control Center.

Gesture detection runs only when the device’s active format supports reaction effects, which you determine by querying the value of the format’s [`reactionEffectsSupported`](avcapturedevice/format/reactioneffectssupported.md) property.

This property is key-value observable.

> **Note**:  Your app can call [`performEffect(for:)`](avcapturedevice/performeffect(for:).md)independently the value of this property. The system intermixes reaction effects from either source.

## See Also

- [class var reactionEffectsEnabled: Bool](avcapturedevice/reactioneffectsenabled.md)
  A Boolean value that indicates whether the app supports performing reaction effects.
- [var canPerformReactionEffects: Bool](avcapturedevice/canperformreactioneffects.md)
  A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [var availableReactionTypes: Set<AVCaptureReactionType>](avcapturedevice/availablereactiontypes.md)
  A set of reactions types that a device supports performing.
- [func performEffect(for: AVCaptureReactionType)](avcapturedevice/performeffect(for:).md)
  Performs the specified reaction type on the video stream.
- [var reactionEffectsInProgress: [AVCaptureReactionEffectState]](avcapturedevice/reactioneffectsinprogress.md)
  An array of reaction effects that the device is currently performing, sorted by timestamp.
- [class AVCaptureReactionEffectState](avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/reactioneffectgesturesenabled)*