# GKChallengeState

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The state of a challenge.

**Availability**:
- iOS 6.0+ - Deprecated in 26.0
- iPadOS 6.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
enum GKChallengeState
```

```c
enum GKChallengeState : NSInteger;
```

## Topics

### Challenge States
- [GKChallengeState.invalid](./gkchallengestate/invalid.md)
  The challenge isn’t valid because an error occurred.
- [GKChallengeState.pending](./gkchallengestate/pending.md)
  The player issued a challenge, but the other player hasn’t accepted or refused it.
- [GKChallengeState.completed](./gkchallengestate/completed.md)
  The player successfully completed the challenge.
- [GKChallengeState.declined](./gkchallengestate/declined.md)
  The player declined the challenge.
### Initializers
- [init?(rawValue: Int)](./gkchallengestate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Examining Details about a Challenge
- [var issuingPlayer: GKPlayer?](./gkchallenge/issuingplayer.md)
  The player who issues the challenge.
- [var receivingPlayer: GKPlayer?](./gkchallenge/receivingplayer.md)
  The player who receives the challenge.
- [var message: String?](./gkchallenge/message.md)
  A text message that describes the challenge.
- [var state: GKChallengeState](./gkchallenge/state.md)
  The current state of the challenge.
- [var issueDate: Date](./gkchallenge/issuedate.md)
  The date the player issued the challenge.
- [var completionDate: Date?](./gkchallenge/completiondate.md)
  The date the challenged player completed the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengestate)*