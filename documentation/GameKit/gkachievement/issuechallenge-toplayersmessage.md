# issueChallenge(toPlayers:message:)

**Framework**: GameKit  
**Kind**: method

Issues an achievement challenge to a list of players.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func issueChallenge(toPlayers playerIDs: [String]?, message: String?)
```

#### Discussion

Set up your game to issue a challenge request only in direct response to a player action.

If you mark the achievement as hidden, or if the challenged player already earned the achievement and you don’t mark the achievement as replayable in App Store Connect, the local player can’t issue the challenge.

## Parameters

- `playerIDs`: The identifiers for the players to challenge. Because Game Center limits the number of players in a challenge request to 10, the maximum size of this array is 10.
- `message`: A text message to display to the challenged players.

## See Also

- [func report(completionHandler: (((any Error)?) -> Void)?)](gkachievement/report(completionhandler:).md)
  Reports the player’s progress to Game Center.
- [func selectChallengeablePlayerIDs([String]?, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](gkachievement/selectchallengeableplayerids(_:withcompletionhandler:).md)
  Finds the subset of players who can earn an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/issuechallenge(toplayers:message:))*