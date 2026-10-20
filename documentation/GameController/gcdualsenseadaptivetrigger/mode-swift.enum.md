# GCDualSenseAdaptiveTrigger.Mode

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

The possible modes of an adaptive trigger.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
enum Mode
```

```c
enum GCDualSenseAdaptiveTriggerMode : NSInteger;
```

## Topics

### Modes
- [GCDualSenseAdaptiveTrigger.Mode.off](./mode-swift.enum/off.md)
  Provides no adaptive trigger effects.
- [GCDualSenseAdaptiveTrigger.Mode.feedback](./mode-swift.enum/feedback.md)
  Provides feedback when the user depresses the trigger equal to, or greater than, the start position.
- [GCDualSenseAdaptiveTrigger.Mode.weapon](./mode-swift.enum/weapon.md)
  Provides feedback when the user depresses the trigger between the start and the end positions.
- [GCDualSenseAdaptiveTrigger.Mode.vibration](./mode-swift.enum/vibration.md)
  Vibrates when the user depresses the trigger equal to, or greater than, the start position.
- [GCDualSenseAdaptiveTrigger.Mode.slopeFeedback](./mode-swift.enum/slopefeedback.md)
  Provides feedback when the user tilts the trigger between the start and the end positions.
### Initializers
- [init?(rawValue: Int)](./mode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the mode
- [var mode: GCDualSenseAdaptiveTrigger.Mode](./mode-swift.property.md)
  The current configuration of the adaptive trigger.
- [func setModeOff()](./setmodeoff%28%29.md)
  Sets the mode to off and stops any trigger effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/mode-swift.enum)*