# player(_:wantsToPlay:)

**Framework**: GameKit  
**Kind**: method

Handles when the local player issues a challenge and the other player accepts.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, wantsToPlay challenge: GKChallenge)
```

## Parameters

- `player`: The player who accepts the challenge.
- `challenge`: The challenge that the player issues to another player.

## See Also

- [func player(GKPlayer, didReceive: GKChallenge)](gkchallengelistener/player(_:didreceive:).md)
  Handles when the local player issues a challenge but the other player doesn’t want to respond immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener/player(_:wantstoplay:))*