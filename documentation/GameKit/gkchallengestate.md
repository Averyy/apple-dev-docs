# GKChallengeState

**Framework**: GameKit  
**Kind**: enum

The state of a challenge.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKChallengeState
```

## Topics

### Challenge States
- [GKChallengeState.invalid](gkchallengestate/invalid.md)
  The challenge isn’t valid because an error occurred.
- [GKChallengeState.pending](gkchallengestate/pending.md)
  The player issued a challenge, but the other player hasn’t accepted or refused it.
- [GKChallengeState.completed](gkchallengestate/completed.md)
  The player successfully completed the challenge.
- [GKChallengeState.declined](gkchallengestate/declined.md)
  The player declined the challenge.
### Initializers
- [init?(rawValue: Int)](gkchallengestate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var issuingPlayer: GKPlayer?](gkchallenge/issuingplayer.md)
  The player who issues the challenge.
- [var receivingPlayer: GKPlayer?](gkchallenge/receivingplayer.md)
  The player who receives the challenge.
- [var message: String?](gkchallenge/message.md)
  A text message that describes the challenge.
- [var state: GKChallengeState](gkchallenge/state.md)
  The current state of the challenge.
- [var issueDate: Date](gkchallenge/issuedate.md)
  The date the player issued the challenge.
- [var completionDate: Date?](gkchallenge/completiondate.md)
  The date the challenged player completed the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengestate)*