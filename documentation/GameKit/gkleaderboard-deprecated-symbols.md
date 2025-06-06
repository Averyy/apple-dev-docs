# Deprecated symbols

**Framework**: GameKit

Review unsupported symbols and their replacements.

## Topics

### Deprecated initializers
- [init?(playerIDs: [String]?)](gkleaderboard/init(playerids:).md)
  Initializes a leaderboard request to retrieve the scores of a specific group of players.
- [init(players: [GKPlayer])](gkleaderboard/init(players:).md)
  Initializes a leaderboard request to retrieve the scores of a specific group of players.
### Deprecated properties
- [var category: String?](gkleaderboard/category.md)
  The named leaderboard to retrieve information from.
- [var identifier: String?](gkleaderboard/identifier.md)
  The named leaderboard to retrieve information from.
- [var isLoading: Bool](gkleaderboard/isloading.md)
  A Boolean value that indicates whether the leaderboard object is retrieving scores.
- [var localPlayerScore: GKScore?](gkleaderboard/localplayerscore.md)
  The score that the local player earns.
- [var maxRange: Int](gkleaderboard/maxrange.md)
  The size of the leaderboard.
- [var playerScope: GKLeaderboard.PlayerScope](gkleaderboard/playerscope-swift.property.md)
  A filter that restricts the search to a subset of the players in Game Center.
- [var range: NSRange](gkleaderboard/range.md)
  The numerical score rankings to return from the search.
- [var scores: [GKScore]?](gkleaderboard/scores.md)
  An array of scores that contains the scores that the search returns.
- [var timeScope: GKLeaderboard.TimeScope](gkleaderboard/timescope-swift.property.md)
  A filter that restricts the search to scores within a specific period of time.
### Deprecated methods
- [class func setDefault(String?, withCompletionHandler: (((any Error)?) -> Void)?)](gkleaderboard/setdefault(_:withcompletionhandler:).md)
  Sets the default leaderboard for the local player.
- [class func loadCategories(completionHandler: (([String]?, [String]?, (any Error)?) -> Void)?)](gkleaderboard/loadcategories(completionhandler:).md)
  Loads the list of leaderboard categories along with their corresponding localized titles.
- [class func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](gkleaderboard/loadleaderboards(completionhandler:).md)
  Loads a list of leaderboards from Game Center.
- [func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)?)](gkleaderboard/loadscores(completionhandler:).md)
  Retrieves a set of scores from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard-deprecated-symbols)*