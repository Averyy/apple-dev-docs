# isLoading

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether the leaderboard object is retrieving scores.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isLoading: Bool { get }
```

#### Discussion

The value of the `loading` property is [`true`](https://developer.apple.com/documentation/Swift/true) if the leaderboard object has any pending requests for scores.

## See Also

- [var category: String?](gkleaderboard/category.md)
  The named leaderboard to retrieve information from.
- [var identifier: String?](gkleaderboard/identifier.md)
  The named leaderboard to retrieve information from.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/isloading)*