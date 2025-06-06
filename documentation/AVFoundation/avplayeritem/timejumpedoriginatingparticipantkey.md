# timeJumpedOriginatingParticipantKey

**Framework**: AVFoundation  
**Kind**: property

A key to retrieve a unique identifier of the participant that caused the time jump.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class let timeJumpedOriginatingParticipantKey: String
```

#### Discussion

Use this key to retrieve a UUID value for the participant in a coordinated playback session that caused the time jump. The returned UUID reresents a value in the playback coordinator’s [`otherParticipants`](avplaybackcoordinator/otherparticipants.md) array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/timejumpedoriginatingparticipantkey)*