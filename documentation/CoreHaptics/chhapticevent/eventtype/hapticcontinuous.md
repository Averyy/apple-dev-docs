# hapticContinuous

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

A haptic event with a looped waveform of arbitrary length.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let hapticContinuous: CHHapticEvent.EventType
```

```c
extern CHHapticEventType CHHapticEventTypeHapticContinuous;
```

#### Discussion

Continuous haptic patterns, like the sustained vibration from a ringtone, take the form of lengthier feedback over a period of time. You must provide continuous events with a duration to determine their endpoint. The maximum duration of a continuous haptic event is 30 seconds.

## See Also

### Enumerating Haptic Types
- [static let audioContinuous: CHHapticEvent.EventType](./audiocontinuous.md)
  An audio event with a looped waveform of arbitrary length.
- [static let audioCustom: CHHapticEvent.EventType](./audiocustom.md)
  An audio event using a waveform that you supply.
- [static let hapticTransient: CHHapticEvent.EventType](./haptictransient.md)
  A brief impulse occurring at a specific point in time, like the feedback from toggling a switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype/hapticcontinuous)*