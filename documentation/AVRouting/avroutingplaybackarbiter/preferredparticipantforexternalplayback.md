# preferredParticipantForExternalPlayback

**Framework**: AVRouting  
**Kind**: property

The participant that has priority to play on external playback interfaces.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
weak var preferredParticipantForExternalPlayback: (any AVRoutingPlaybackParticipant)? { get set }
```

#### Discussion

This participant takes precedence over all others to play on external playback interfaces (specifically for AirPlay video and Apple Lightning Digital AV Adapters).

By default, this value is `nil`. When the value is `nil`, the arbiter doesn’t impose any priority on the participants, and the participant that is selected to playback externally falls back to the existing selection mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avroutingplaybackarbiter/preferredparticipantforexternalplayback)*