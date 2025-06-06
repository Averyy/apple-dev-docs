# GCDualSenseAdaptiveTrigger.Mode

**Framework**: Game Controller  
**Kind**: enum

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

## Topics

### Modes
- [GCDualSenseAdaptiveTrigger.Mode.off](gcdualsenseadaptivetrigger/mode-swift.enum/off.md)
  Provides no adaptive trigger effects.
- [GCDualSenseAdaptiveTrigger.Mode.feedback](gcdualsenseadaptivetrigger/mode-swift.enum/feedback.md)
  Provides feedback when the user depresses the trigger equal to, or greater than, the start position.
- [GCDualSenseAdaptiveTrigger.Mode.weapon](gcdualsenseadaptivetrigger/mode-swift.enum/weapon.md)
  Provides feedback when the user depresses the trigger between the start and the end positions.
- [GCDualSenseAdaptiveTrigger.Mode.vibration](gcdualsenseadaptivetrigger/mode-swift.enum/vibration.md)
  Vibrates when the user depresses the trigger equal to, or greater than, the start position.
- [GCDualSenseAdaptiveTrigger.Mode.slopeFeedback](gcdualsenseadaptivetrigger/mode-swift.enum/slopefeedback.md)
  Provides feedback when the user tilts the trigger between the start and the end positions.
### Initializers
- [init?(rawValue: Int)](gcdualsenseadaptivetrigger/mode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var mode: GCDualSenseAdaptiveTrigger.Mode](gcdualsenseadaptivetrigger/mode-swift.property.md)
  The current configuration of the adaptive trigger.
- [func setModeOff()](gcdualsenseadaptivetrigger/setmodeoff.md)
  Sets the mode to off and stops any trigger effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/mode-swift.enum)*