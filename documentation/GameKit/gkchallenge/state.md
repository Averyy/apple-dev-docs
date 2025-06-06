# state

**Framework**: GameKit  
**Kind**: property

The current state of the challenge.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var state: GKChallengeState { get }
```

#### Discussion

See [`GKChallengeState`](gkchallengestate.md) for possible values.

## See Also

- [var issuingPlayer: GKPlayer?](gkchallenge/issuingplayer.md)
  The player who issues the challenge.
- [var receivingPlayer: GKPlayer?](gkchallenge/receivingplayer.md)
  The player who receives the challenge.
- [var message: String?](gkchallenge/message.md)
  A text message that describes the challenge.
- [enum GKChallengeState](gkchallengestate.md)
  The state of a challenge.
- [var issueDate: Date](gkchallenge/issuedate.md)
  The date the player issued the challenge.
- [var completionDate: Date?](gkchallenge/completiondate.md)
  The date the challenged player completed the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge/state)*