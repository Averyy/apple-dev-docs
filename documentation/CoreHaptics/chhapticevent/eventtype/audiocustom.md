# audioCustom

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

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

```c
extern CHHapticEventType CHHapticEventTypeAudioCustom;
```

#### Discussion

Custom waveforms behave like transient events, with no looping.

## See Also

### Enumerating Haptic Types
- [static let audioContinuous: CHHapticEvent.EventType](./audiocontinuous.md)
  An audio event with a looped waveform of arbitrary length.
- [static let hapticTransient: CHHapticEvent.EventType](./haptictransient.md)
  A brief impulse occurring at a specific point in time, like the feedback from toggling a switch.
- [static let hapticContinuous: CHHapticEvent.EventType](./hapticcontinuous.md)
  A haptic event with a looped waveform of arbitrary length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype/audiocustom)*