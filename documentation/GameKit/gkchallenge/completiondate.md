# completionDate

**Framework**: GameKit  
**Kind**: property

The date the challenged player completed the challenge.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var completionDate: Date? { get }
```

#### Discussion

The value of this property is `nil` until the challenged player completes it.

## See Also

- [var issuingPlayer: GKPlayer?](gkchallenge/issuingplayer.md)
  The player who issues the challenge.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge/completiondate)*