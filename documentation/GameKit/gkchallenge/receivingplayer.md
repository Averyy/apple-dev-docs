# receivingPlayer

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The player who receives the challenge.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.10+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
@NSCopying
var receivingPlayer: GKPlayer? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) GKPlayer * receivingPlayer;
```

## See Also

### Examining Details about a Challenge
- [var issuingPlayer: GKPlayer?](./issuingplayer.md)
  The player who issues the challenge.
- [var message: String?](./message.md)
  A text message that describes the challenge.
- [var state: GKChallengeState](./state.md)
  The current state of the challenge.
- [enum GKChallengeState](../gkchallengestate.md)
  The state of a challenge.
- [var issueDate: Date](./issuedate.md)
  The date the player issued the challenge.
- [var completionDate: Date?](./completiondate.md)
  The date the challenged player completed the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge/receivingplayer)*