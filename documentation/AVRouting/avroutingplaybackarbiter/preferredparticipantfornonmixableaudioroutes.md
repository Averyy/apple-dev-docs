# preferredParticipantForNonMixableAudioRoutes

**Framework**: AVRouting  
**Kind**: property

The participant that has priority to play audio when it’s not possible to play multiple audio sources concurrently.

**Availability**:
- tvOS 26.0+

## Declaration

```swift
weak var preferredParticipantForNonMixableAudioRoutes: (any AVRoutingPlaybackParticipant)? { get set }
```

#### Discussion

This participant takes precedence over all other participants to play audio in non-mixable audio routes when concurrent audio playback isn’t possible, and only a single participant can play audio. The system unmutes this participant’s audio, and mutes the audio of all other participants.

By default, this value is `nil`. When the current preferred participant finishes, the system sets this value to `nil`. If this value is `nil`, the arbiter doesn’t impose any priority on the participants, and the participant that’s unmuted is based on the existing selection mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avroutingplaybackarbiter/preferredparticipantfornonmixableaudioroutes)*