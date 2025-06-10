# CHHapticEvent.ParameterID

**Framework**: Core Haptics  
**Kind**: struct

An identifier for an event parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct ParameterID
```

## Mentions

- [Representing haptic patterns in AHAP files](representing-haptic-patterns-in-ahap-files.md)

#### Discussion

Specify event parameters when creating a haptic or audio event. The combination of parameters determines the event’s character.

## Topics

### Haptic Event Parameter IDs
- [static let hapticIntensity: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticintensity.md)
  The strength of a haptic event.
- [static let hapticSharpness: CHHapticEvent.ParameterID](chhapticevent/parameterid/hapticsharpness.md)
  The feel of a haptic event.
- [static let attackTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/attacktime.md)
  The time at which a haptic pattern’s intensity begins increasing.
- [static let decayTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/decaytime.md)
  The time at which a haptic pattern’s intensity begins decreasing.
- [static let releaseTime: CHHapticEvent.ParameterID](chhapticevent/parameterid/releasetime.md)
  The time at which to begin fading the haptic pattern.
- [static let sustained: CHHapticEvent.ParameterID](chhapticevent/parameterid/sustained.md)
  A Boolean value that indicates whether to sustain a haptic event for its specified duration.
### Audio Event Parameter IDs
- [static let audioVolume: CHHapticEvent.ParameterID](chhapticevent/parameterid/audiovolume.md)
  The volume of an audio event.
- [static let audioPan: CHHapticEvent.ParameterID](chhapticevent/parameterid/audiopan.md)
  The stereo panning of an audio event.
- [static let audioPitch: CHHapticEvent.ParameterID](chhapticevent/parameterid/audiopitch.md)
  The pitch of an audio event.
- [static let audioBrightness: CHHapticEvent.ParameterID](chhapticevent/parameterid/audiobrightness.md)
  The high-frequency content of an audio event.
### Swift Initializers
- [init(rawValue: String)](chhapticevent/parameterid/init(rawvalue:).md)
  Creates the identifier of a haptic event parameter with the specified string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var eventParameters: [CHHapticEventParameter]](chhapticevent/eventparameters.md)
  An array of event parameters, possibly empty.
- [var relativeTime: TimeInterval](chhapticevent/relativetime.md)
  The start time of the event, relative to other events in the same pattern.
- [var duration: TimeInterval](chhapticevent/duration.md)
  The duration of the haptic event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/parameterid)*