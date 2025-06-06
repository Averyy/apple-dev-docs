# GKChallengeListener

**Framework**: GameKit  
**Kind**: protocol

An object that responds to challenge events.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol GKChallengeListener : NSObjectProtocol
```

#### Overview

Your game can ignore a challenge, start up in a specific state so the local player can respond to a challenge, or notify the challenger when the local player completes a challenge.

Don’t implement [`GKChallengeListener`](gkchallengelistener.md) directly; instead use [`GKLocalPlayerListener`](gklocalplayerlistener.md). The [`GKLocalPlayerListener`](gklocalplayerlistener.md) protocol inherits methods from [`GKChallengeListener`](gkchallengelistener.md), [`GKInviteEventListener`](gkinviteeventlistener.md), [`GKSavedGameListener`](gksavedgamelistener.md), and [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) in order to handle multiple events.

## Topics

### Responding to a Challenge
- [func player(GKPlayer, didReceive: GKChallenge)](gkchallengelistener/player(_:didreceive:).md)
  Handles when the local player issues a challenge but the other player doesn’t want to respond immediately.
- [func player(GKPlayer, wantsToPlay: GKChallenge)](gkchallengelistener/player(_:wantstoplay:).md)
  Handles when the local player issues a challenge and the other player accepts.
### Completing a Challenge
- [func player(GKPlayer, didComplete: GKChallenge, issuedByFriend: GKPlayer)](gkchallengelistener/player(_:didcomplete:issuedbyfriend:).md)
  Handles when the local player completes a challenge that a friend issues.
- [func player(GKPlayer, issuedChallengeWasCompleted: GKChallenge, byFriend: GKPlayer)](gkchallengelistener/player(_:issuedchallengewascompleted:byfriend:).md)
  Handles when a friend completes a challenge that the local player issues.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [GKLocalPlayerListener](gklocalplayerlistener.md)

## See Also

- [class GKChallenge](gkchallenge.md)
  A challenge issued by the local player to another player.
- [class GKScoreChallenge](gkscorechallenge.md)
  A type of challenge where a player must beat the leaderboard score of another player.
- [class GKAchievementChallenge](gkachievementchallenge.md)
  A type of challenge where a player must earn another player’s achievement.
- [GKShowChallengeBanners](../BundleResources/Information-Property-List/GKShowChallengeBanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener)*