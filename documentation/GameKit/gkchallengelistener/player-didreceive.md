# player(_:didReceive:)

**Framework**: GameKit  
**Kind**: method

Handles when the local player issues a challenge but the other player doesn’t want to respond immediately.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, didReceive challenge: GKChallenge)
```

## Parameters

- `player`: The player who receives the challenge.
- `challenge`: The challenge that the player issues to another player.

## See Also

- [func player(GKPlayer, wantsToPlay: GKChallenge)](gkchallengelistener/player(_:wantstoplay:).md)
  Handles when the local player issues a challenge and the other player accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener/player(_:didreceive:))*