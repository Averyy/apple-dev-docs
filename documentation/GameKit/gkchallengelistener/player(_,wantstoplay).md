# player(_:wantsToPlay:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when the local player issues a challenge and the other player accepts.

**Availability**:
- iOS 7.0+ - Deprecated in 26.0
- iPadOS 7.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.10+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
optional func player(_ player: GKPlayer, wantsToPlay challenge: GKChallenge)
```

```objc
- (void) player:(GKPlayer *) player wantsToPlayChallenge:(GKChallenge *) challenge;
```

## Parameters

- `player`: The player who accepts the challenge.
- `challenge`: The challenge that the player issues to another player.

## See Also

### Responding to a Challenge
- [func player(GKPlayer, didReceive: GKChallenge)](./player%28_,didreceive%29.md)
  Handles when the local player issues a challenge but the other player doesn’t want to respond immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener/player(_:wantstoplay:))*