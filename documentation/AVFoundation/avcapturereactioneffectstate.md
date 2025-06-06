# AVCaptureReactionEffectState

**Framework**: AVFoundation  
**Kind**: class

An object that reports the state of a reaction effect performed on a capture device.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureReactionEffectState
```

#### Overview

Obtain an instance of this class by querying a capture device’s [`reactionEffectsInProgress`](avcapturedevice/reactioneffectsinprogress.md) property. The system adds new entries to this array when you call [`performEffect(for:)`](avcapturedevice/performeffect(for:).md) or by gesture detection in the capture stream when the value of [`reactionEffectGesturesEnabled`](avcapturedevice/reactioneffectgesturesenabled.md) is [`true`](https://developer.apple.com/documentation/swift/true).

The system renders the effect before providing frames to your app, and these status objects let you know when it performs the effect.

## Topics

### Configuring the effect state
- [var reactionType: AVCaptureReactionType](avcapturereactioneffectstate/reactiontype.md)
  The type of reaction.
- [struct AVCaptureReactionType](avcapturereactiontype.md)
  Constants that indicate the type of reaction that an effect can perform.
- [var startTime: CMTime](avcapturereactioneffectstate/starttime.md)
  The presentation time of the first frame where the system renders the effect.
- [var endTime: CMTime](avcapturereactioneffectstate/endtime.md)
  The presentation time of the first frame following the end of a reaction effect.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [var reactionEffectsInProgress: [AVCaptureReactionEffectState]](avcapturedevice/reactioneffectsinprogress.md)
  An array of reaction effects that the device is currently performing, sorted by timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturereactioneffectstate)*