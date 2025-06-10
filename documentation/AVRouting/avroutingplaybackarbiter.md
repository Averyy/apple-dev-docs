# AVRoutingPlaybackArbiter

**Framework**: AVRouting  
**Kind**: class

An object that manages playback routing preferences.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
class AVRoutingPlaybackArbiter
```

#### Overview

This object manages instances of [`AVRoutingPlaybackParticipant`](avroutingplaybackparticipant.md) for arbitration of media playback routing priorities and preferences on restricted playback interfaces. The playback routing arbiter is responsible for collecting and applying preferences, such as priorities in non-mixable audio routes and external playback states where the number of allowed players is limited.

## Topics

### Instance Properties
- [var preferredParticipantForExternalPlayback: (any AVRoutingPlaybackParticipant)?](avroutingplaybackarbiter/preferredparticipantforexternalplayback.md)
  The participant that has priority to play on external playback interfaces.
- [var preferredParticipantForNonMixableAudioRoutes: (any AVRoutingPlaybackParticipant)?](avroutingplaybackarbiter/preferredparticipantfornonmixableaudioroutes.md)
  The participant that has priority to play audio when it’s not possible to play multiple audio sources concurrently.
### Type Methods
- [class func shared() -> AVRoutingPlaybackArbiter](avroutingplaybackarbiter/shared.md)
  Returns the singleton playback arbiter instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol AVRoutingPlaybackParticipant](avroutingplaybackparticipant.md)
  A protocol for objects that participate in playback routing arbitration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avroutingplaybackarbiter)*