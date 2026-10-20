# player(_:didComplete:issuedByFriend:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when the local player completes a challenge that a friend issues.

**Availability**:
- iOS 7.0+ - Deprecated in 26.0
- iPadOS 7.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.10+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
optional func player(_ player: GKPlayer, didComplete challenge: GKChallenge, issuedByFriend friendPlayer: GKPlayer)
```

```objc
- (void) player:(GKPlayer *) player didCompleteChallenge:(GKChallenge *) challenge issuedByFriend:(GKPlayer *) friendPlayer;
```

## Parameters

- `player`: The player who completes the challenge.
- `challenge`: The challenge that the player completes.
- `friendPlayer`: The friend who issues the challenge.

## See Also

### Completing a Challenge
- [func player(GKPlayer, issuedChallengeWasCompleted: GKChallenge, byFriend: GKPlayer)](./player%28_,issuedchallengewascompleted,byfriend%29.md)
  Handles when a friend completes a challenge that the local player issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener/player(_:didcomplete:issuedbyfriend:))*