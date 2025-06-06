# Deprecated Symbols

**Framework**: GameKit

Review unsupported symbols and their replacements.

## Topics

### Deprecated Initializers
- [init?(identifier: String?, forPlayer: String)](gkachievement/init(identifier:forplayer:).md)
  Initializes an achievement for a specific player.
### Deprecated Methods
- [func issueChallenge(toPlayers: [String]?, message: String?)](gkachievement/issuechallenge(toplayers:message:).md)
  Issues an achievement challenge to a list of players.
- [func report(completionHandler: (((any Error)?) -> Void)?)](gkachievement/report(completionhandler:).md)
  Reports the player’s progress to Game Center.
- [func selectChallengeablePlayerIDs([String]?, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](gkachievement/selectchallengeableplayerids(_:withcompletionhandler:).md)
  Finds the subset of players who can earn an achievement.
### Deprecated Properties
- [var isHidden: Bool](gkachievement/ishidden.md)
  A Boolean value that indicates whether the system hides this achievement from the player.
- [var playerID: String?](gkachievement/playerid.md)
  A string that identifies the player who earned the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement-deprecated-symbols)*