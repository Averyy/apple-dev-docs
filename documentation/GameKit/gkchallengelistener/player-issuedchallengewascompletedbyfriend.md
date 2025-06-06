# player(_:issuedChallengeWasCompleted:byFriend:)

**Framework**: GameKit  
**Kind**: method

Handles when a friend completes a challenge that the local player issues.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, issuedChallengeWasCompleted challenge: GKChallenge, byFriend friendPlayer: GKPlayer)
```

## Parameters

- `player`: The player who issues the challenge.
- `challenge`: The challenge that the friend completes.
- `friendPlayer`: The player who completes the challenge.

## See Also

- [func player(GKPlayer, didComplete: GKChallenge, issuedByFriend: GKPlayer)](gkchallengelistener/player(_:didcomplete:issuedbyfriend:).md)
  Handles when the local player completes a challenge that a friend issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener/player(_:issuedchallengewascompleted:byfriend:))*