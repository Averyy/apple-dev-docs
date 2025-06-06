# CHHapticEvent.EventType

**Framework**: Core Haptics  
**Kind**: struct

The types of audio and haptic event waveforms.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct EventType
```

## Mentions

- [Representing haptic patterns in AHAP files](representing-haptic-patterns-in-ahap-files.md)

## Topics

### Specifying a Type
- [init(rawValue: String)](chhapticevent/eventtype/init(rawvalue:).md)
  Initializes an event type from a raw string value.
### Enumerating Haptic Types
- [static let audioContinuous: CHHapticEvent.EventType](chhapticevent/eventtype/audiocontinuous.md)
  An audio event with a looped waveform of arbitrary length.
- [static let audioCustom: CHHapticEvent.EventType](chhapticevent/eventtype/audiocustom.md)
  An audio event using a waveform that you supply.
- [static let hapticTransient: CHHapticEvent.EventType](chhapticevent/eventtype/haptictransient.md)
  A brief impulse occurring at a specific point in time, like the feedback from toggling a switch.
- [static let hapticContinuous: CHHapticEvent.EventType](chhapticevent/eventtype/hapticcontinuous.md)
  A haptic event with a looped waveform of arbitrary length.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var type: CHHapticEvent.EventType](chhapticevent/type.md)
  The type of the haptic event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype)*