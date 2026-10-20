# canPerformReactionEffects

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can perform reaction effects on a capture device.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var canPerformReactionEffects: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canPerformReactionEffects;
```

#### Discussion

This value is [`true`](../../Swift/true.md) when a device’s [`reactionEffectsEnabled`](./reactioneffectsenabled.md) and its active format’s [`reactionEffectsSupported`](./format/reactioneffectssupported.md) property values are [`true`](../../Swift/true.md).

## See Also

### Performing reaction effects
- [class var reactionEffectsEnabled: Bool](./reactioneffectsenabled.md)
  A Boolean value that indicates whether the app supports performing reaction effects.
- [var availableReactionTypes: Set<AVCaptureReactionType>](./availablereactiontypes.md)
  A set of reactions types that a device supports performing.
- [class var reactionEffectGesturesEnabled: Bool](./reactioneffectgesturesenabled.md)
  A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [func performEffect(for: AVCaptureReactionType)](./performeffect%28for%29.md)
  Performs the specified reaction type on the video stream.
- [var reactionEffectsInProgress: [AVCaptureReactionEffectState]](./reactioneffectsinprogress.md)
  An array of reaction effects that the device is currently performing, sorted by timestamp.
- [class AVCaptureReactionEffectState](../avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/canperformreactioneffects)*