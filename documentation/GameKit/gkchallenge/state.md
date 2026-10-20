# state

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The current state of the challenge.

**Availability**:
- iOS 6.0+ - Deprecated in 26.0
- iPadOS 6.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
var state: GKChallengeState { get }
```

```objc
@property (nonatomic, assign, readonly) GKChallengeState state;
```

#### Discussion

See [`GKChallengeState`](../gkchallengestate.md) for possible values.

## See Also

### Examining Details about a Challenge
- [var issuingPlayer: GKPlayer?](./issuingplayer.md)
  The player who issues the challenge.
- [var receivingPlayer: GKPlayer?](./receivingplayer.md)
  The player who receives the challenge.
- [var message: String?](./message.md)
  A text message that describes the challenge.
- [enum GKChallengeState](../gkchallengestate.md)
  The state of a challenge.
- [var issueDate: Date](./issuedate.md)
  The date the player issued the challenge.
- [var completionDate: Date?](./completiondate.md)
  The date the challenged player completed the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge/state)*