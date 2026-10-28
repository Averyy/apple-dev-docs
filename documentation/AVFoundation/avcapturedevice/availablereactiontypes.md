# availableReactionTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSSet<NSString *> * availableReactionTypes;
```

## Discussion

The list may differ between devices, and may change for a specific device when it’s active format changes.

This property is key-value observable.

## See Also

### Performing reaction effects
- [class var reactionEffectsEnabled: Bool](./reactioneffectsenabled.md)
  A Boolean value that indicates whether the app supports performing reaction effects.
- [var canPerformReactionEffects: Bool](./canperformreactioneffects.md)
  A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [class var reactionEffectGesturesEnabled: Bool](./reactioneffectgesturesenabled.md)
  A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [func performEffect(for: AVCaptureReactionType)](./performeffect%28for%29.md)
  Performs the specified reaction type on the video stream.
- [var reactionEffectsInProgress: [AVCaptureReactionEffectState]](./reactioneffectsinprogress.md)
  An array of reaction effects that the device is currently performing, sorted by timestamp.
- [class AVCaptureReactionEffectState](../avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/availablereactiontypes)*