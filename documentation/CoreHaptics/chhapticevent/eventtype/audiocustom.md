# audioCustom

**Framework**: Core Haptics  
**Kind**: property

An audio event using a waveform that you supply.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let audioCustom: CHHapticEvent.EventType
```

#### Discussion

Custom waveforms behave like transient events, with no looping.

## See Also

- [static let audioContinuous: CHHapticEvent.EventType](chhapticevent/eventtype/audiocontinuous.md)
  An audio event with a looped waveform of arbitrary length.
- [static let hapticTransient: CHHapticEvent.EventType](chhapticevent/eventtype/haptictransient.md)
  A brief impulse occurring at a specific point in time, like the feedback from toggling a switch.
- [static let hapticContinuous: CHHapticEvent.EventType](chhapticevent/eventtype/hapticcontinuous.md)
  A haptic event with a looped waveform of arbitrary length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype/audiocustom)*