# reactionEffectsInProgress

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<AVCaptureReactionEffectState *> * reactionEffectsInProgress;
```

#### Discussion

Key-value observe this property to determine when reaction effects begin and end. If your key-value observing callback provides old and new values, any in-progress reaction effects in the new array have a value of [`invalid`](../../CoreMedia/cmtime/invalid.md) for their [`endTime`](../avcapturereactioneffectstate/endtime.md) property value. Completed reaction effects are only in the old array, and have their [`endTime`](../avcapturereactioneffectstate/endtime.md) property value set to the presentation time of the first frame where the reaction effect was no longer present.

## See Also

### Performing reaction effects
- [class var reactionEffectsEnabled: Bool](./reactioneffectsenabled.md)
  A Boolean value that indicates whether the app supports performing reaction effects.
- [var canPerformReactionEffects: Bool](./canperformreactioneffects.md)
  A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [var availableReactionTypes: Set<AVCaptureReactionType>](./availablereactiontypes.md)
  A set of reactions types that a device supports performing.
- [class var reactionEffectGesturesEnabled: Bool](./reactioneffectgesturesenabled.md)
  A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [func performEffect(for: AVCaptureReactionType)](./performeffect%28for%29.md)
  Performs the specified reaction type on the video stream.
- [class AVCaptureReactionEffectState](../avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/reactioneffectsinprogress)*