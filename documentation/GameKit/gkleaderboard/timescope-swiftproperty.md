# timeScope

**Framework**: GameKit  
**Kind**: property

A filter that restricts the search to scores within a specific period of time.

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
var timeScope: GKLeaderboard.TimeScope { get set }
```

#### Discussion

This property determines how far back in time to look for scores. The default value is [`GKLeaderboard.TimeScope.allTime`](gkleaderboard/timescope-swift.enum/alltime.md). See [`GKLeaderboard.TimeScope`](gkleaderboard/timescope-swift.enum.md) for more information.

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
- [var playerScope: GKLeaderboard.PlayerScope](gkleaderboard/playerscope-swift.property.md)
  A filter that restricts the search to a subset of the players in Game Center.
- [var range: NSRange](gkleaderboard/range.md)
  The numerical score rankings to return from the search.
- [var scores: [GKScore]?](gkleaderboard/scores.md)
  An array of scores that contains the scores that the search returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/timescope-swift.property)*