# playerScope

**Framework**: GameKit  
**Kind**: property

A filter that restricts the search to a subset of the players in Game Center.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var playerScope: GKLeaderboard.PlayerScope { get set }
```

#### Discussion

GameKit ignores the [`playerScope`](gkleaderboard/playerscope-swift.property.md) property if the leaderboard request initializes using the [`init(playerIDs:)`](gkleaderboard/init(playerids:).md) method. Otherwise, the [`playerScope`](gkleaderboard/playerscope-swift.property.md) property determines which players to include in the request for high scores. The default is [`GKLeaderboard.PlayerScope.global`](gkleaderboard/playerscope-swift.enum/global.md). See [`GKLeaderboard.PlayerScope`](gkleaderboard/playerscope-swift.enum.md) for more information.

## See Also

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
- [var range: NSRange](gkleaderboard/range.md)
  The numerical score rankings to return from the search.
- [var scores: [GKScore]?](gkleaderboard/scores.md)
  An array of scores that contains the scores that the search returns.
- [var timeScope: GKLeaderboard.TimeScope](gkleaderboard/timescope-swift.property.md)
  A filter that restricts the search to scores within a specific period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/playerscope-swift.property)*