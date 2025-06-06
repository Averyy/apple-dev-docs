# range

**Framework**: GameKit  
**Kind**: property

The numerical score rankings to return from the search.

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
var range: NSRange { get set }
```

#### Discussion

GameKit ignores the [`range`](gkleaderboard/range.md) property if the leaderboard request initializes using the [`init(playerIDs:)`](gkleaderboard/init(playerids:).md) method. Otherwise, the [`range`](gkleaderboard/range.md) property filters which scores to return to your game. For example, if you specify a range of `[1,10]`, when the search completes, your game receives the best ten scores. The default range is `[1,25]`.

The minimum index is `1`. The maximum length is `100`.

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
- [var scores: [GKScore]?](gkleaderboard/scores.md)
  An array of scores that contains the scores that the search returns.
- [var timeScope: GKLeaderboard.TimeScope](gkleaderboard/timescope-swift.property.md)
  A filter that restricts the search to scores within a specific period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/range)*