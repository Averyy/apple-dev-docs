# completionDate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The date the challenged player completed the challenge.

**Availability**:
- iOS 6.0+ - Deprecated in 26.0
- iPadOS 6.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
var completionDate: Date? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSDate * completionDate;
```

## Discussion

The value of this property is `nil` until the challenged player completes it.

## See Also

### Examining Details about a Challenge
- [var issuingPlayer: GKPlayer?](./issuingplayer.md)
  The player who issues the challenge.
- [var receivingPlayer: GKPlayer?](./receivingplayer.md)
  The player who receives the challenge.
- [var message: String?](./message.md)
  A text message that describes the challenge.
- [var state: GKChallengeState](./state.md)
  The current state of the challenge.
- [enum GKChallengeState](../gkchallengestate.md)
  The state of a challenge.
- [var issueDate: Date](./issuedate.md)
  The date the player issued the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge/completiondate)*