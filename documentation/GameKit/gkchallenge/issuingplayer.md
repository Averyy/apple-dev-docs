# issuingPlayer

**Framework**: GameKit  
**Kind**: property

The player who issues the challenge.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var issuingPlayer: GKPlayer? { get }
```

## See Also

- [var receivingPlayer: GKPlayer?](gkchallenge/receivingplayer.md)
  The player who receives the challenge.
- [var message: String?](gkchallenge/message.md)
  A text message that describes the challenge.
- [var state: GKChallengeState](gkchallenge/state.md)
  The current state of the challenge.
- [enum GKChallengeState](gkchallengestate.md)
  The state of a challenge.
- [var issueDate: Date](gkchallenge/issuedate.md)
  The date the player issued the challenge.
- [var completionDate: Date?](gkchallenge/completiondate.md)
  The date the challenged player completed the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge/issuingplayer)*