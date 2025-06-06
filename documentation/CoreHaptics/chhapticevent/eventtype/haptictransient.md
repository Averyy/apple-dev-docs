# hapticTransient

**Framework**: Core Haptics  
**Kind**: property

A brief impulse occurring at a specific point in time, like the feedback from toggling a switch.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let hapticTransient: CHHapticEvent.EventType
```

## Mentions

- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)

#### Discussion

Transient events complete on their own, even without a duration.

## See Also

- [static let audioContinuous: CHHapticEvent.EventType](chhapticevent/eventtype/audiocontinuous.md)
  An audio event with a looped waveform of arbitrary length.
- [static let audioCustom: CHHapticEvent.EventType](chhapticevent/eventtype/audiocustom.md)
  An audio event using a waveform that you supply.
- [static let hapticContinuous: CHHapticEvent.EventType](chhapticevent/eventtype/hapticcontinuous.md)
  A haptic event with a looped waveform of arbitrary length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype/haptictransient)*