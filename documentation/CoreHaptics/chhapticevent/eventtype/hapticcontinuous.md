# hapticContinuous

**Framework**: Core Haptics  
**Kind**: property

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

#### Discussion

Continuous haptic patterns, like the sustained vibration from a ringtone, take the form of lengthier feedback over a period of time. You must provide continuous events with a duration to determine their endpoint. The maximum duration of a continuous haptic event is 30 seconds.

## See Also

- [static let audioContinuous: CHHapticEvent.EventType](chhapticevent/eventtype/audiocontinuous.md)
  An audio event with a looped waveform of arbitrary length.
- [static let audioCustom: CHHapticEvent.EventType](chhapticevent/eventtype/audiocustom.md)
  An audio event using a waveform that you supply.
- [static let hapticTransient: CHHapticEvent.EventType](chhapticevent/eventtype/haptictransient.md)
  A brief impulse occurring at a specific point in time, like the feedback from toggling a switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype/hapticcontinuous)*