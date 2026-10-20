# player(_:issuedChallengeWasCompleted:byFriend:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when a friend completes a challenge that the local player issues.

**Availability**:
- iOS 7.0+ - Deprecated in 26.0
- iPadOS 7.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.10+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
optional func player(_ player: GKPlayer, issuedChallengeWasCompleted challenge: GKChallenge, byFriend friendPlayer: GKPlayer)
```

```objc
- (void) player:(GKPlayer *) player issuedChallengeWasCompleted:(GKChallenge *) challenge byFriend:(GKPlayer *) friendPlayer;
```

## Parameters

- `player`: The player who issues the challenge.
- `challenge`: The challenge that the friend completes.
- `friendPlayer`: The player who completes the challenge.

## See Also

### Completing a Challenge
- [func player(GKPlayer, didComplete: GKChallenge, issuedByFriend: GKPlayer)](./player%28_,didcomplete,issuedbyfriend%29.md)
  Handles when the local player completes a challenge that a friend issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener/player(_:issuedchallengewascompleted:byfriend:))*