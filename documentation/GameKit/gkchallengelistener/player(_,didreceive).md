# player(_:didReceive:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when the local player issues a challenge but the other player doesn’t want to respond immediately.

**Availability**:
- iOS 7.0+ - Deprecated in 26.0
- iPadOS 7.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.10+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
optional func player(_ player: GKPlayer, didReceive challenge: GKChallenge)
```

```objc
- (void) player:(GKPlayer *) player didReceiveChallenge:(GKChallenge *) challenge;
```

## Parameters

- `player`: The player who receives the challenge.
- `challenge`: The challenge that the player issues to another player.

## See Also

### Responding to a Challenge
- [func player(GKPlayer, wantsToPlay: GKChallenge)](./player%28_,wantstoplay%29.md)
  Handles when the local player issues a challenge and the other player accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener/player(_:didreceive:))*