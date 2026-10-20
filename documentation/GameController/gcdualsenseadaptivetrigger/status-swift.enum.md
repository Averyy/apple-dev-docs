# GCDualSenseAdaptiveTrigger.Status

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

The possible states of an adaptive trigger.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
enum Status
```

```c
enum GCDualSenseAdaptiveTriggerStatus : NSInteger;
```

## Topics

### Statuses
- [GCDualSenseAdaptiveTrigger.Status.unknown](./status-swift.enum/unknown.md)
  The trigger status is unknown.
- [GCDualSenseAdaptiveTrigger.Status.feedbackNoLoad](./status-swift.enum/feedbacknoload.md)
  The trigger is in feedback mode, but isn’t applying the resistive load.
- [GCDualSenseAdaptiveTrigger.Status.feedbackLoadApplied](./status-swift.enum/feedbackloadapplied.md)
  The trigger is in feedback mode and is applying the resistive load.
- [GCDualSenseAdaptiveTrigger.Status.weaponReady](./status-swift.enum/weaponready.md)
  The trigger is in weapon mode and ready to fire, but isn’t applying the resistive load.
- [GCDualSenseAdaptiveTrigger.Status.weaponFiring](./status-swift.enum/weaponfiring.md)
  The trigger is in weapon mode, firing, and is applying the resistive load.
- [GCDualSenseAdaptiveTrigger.Status.weaponFired](./status-swift.enum/weaponfired.md)
  The trigger is in weapon mode, has fired, and has stopped applying the resistive load.
- [GCDualSenseAdaptiveTrigger.Status.vibrationNotVibrating](./status-swift.enum/vibrationnotvibrating.md)
  The trigger is in vibration mode, but isn’t vibrating.
- [GCDualSenseAdaptiveTrigger.Status.vibrationIsVibrating](./status-swift.enum/vibrationisvibrating.md)
  The trigger is in vibration mode and is vibrating.
- [GCDualSenseAdaptiveTrigger.Status.slopeFeedbackReady](./status-swift.enum/slopefeedbackready.md)
  The trigger is in slope mode, but isn’t applying the resistive load.
- [GCDualSenseAdaptiveTrigger.Status.slopeFeedbackApplyingLoad](./status-swift.enum/slopefeedbackapplyingload.md)
  The trigger is in slope mode, and is applying the resistive load.
- [GCDualSenseAdaptiveTrigger.Status.slopeFeedbackFinished](./status-swift.enum/slopefeedbackfinished.md)
  The trigger is in slope mode, and stopped applying the resistive load.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking the status
- [var status: GCDualSenseAdaptiveTrigger.Status](./status-swift.property.md)
  The current status of the adaptive trigger and whether it’s applying effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/status-swift.enum)*