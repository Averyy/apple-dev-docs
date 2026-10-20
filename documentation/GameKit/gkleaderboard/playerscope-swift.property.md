# playerScope

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A filter that restricts the search to a subset of the players in Game Center.

**Availability**:
- iOS 4.0+ - Deprecated in 14.0
- iPadOS 4.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use the [`loadEntries(for:timeScope:range:completionHandler:)`](./loadentries%28for,timescope,range,completionhandler%29.md) method instead.

## Declaration

```swift
var playerScope: GKLeaderboard.PlayerScope { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign) GKLeaderboardPlayerScope playerScope;
```

*macOS*

```objc
@property (atomic, assign) GKLeaderboardPlayerScope playerScope;
```

#### Discussion

GameKit ignores the [`playerScope`](./playerscope-swift.property.md) property if the leaderboard request initializes using the [`init(playerIDs:)`](./init%28playerids%29.md) method. Otherwise, the [`playerScope`](./playerscope-swift.property.md) property determines which players to include in the request for high scores. The default is [`GKLeaderboard.PlayerScope.global`](./playerscope-swift.enum/global.md). See [`GKLeaderboard.PlayerScope`](./playerscope-swift.enum.md) for more information.

## See Also

### Deprecated properties
- [var category: String?](./category.md)
  The named leaderboard to retrieve information from.
- [var identifier: String?](./identifier.md)
  The named leaderboard to retrieve information from.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the leaderboard object is retrieving scores.
- [var localPlayerScore: GKScore?](./localplayerscore.md)
  The score that the local player earns.
- [var maxRange: Int](./maxrange.md)
  The size of the leaderboard.
- [var range: NSRange](./range.md)
  The numerical score rankings to return from the search.
- [var scores: [GKScore]?](./scores.md)
  An array of scores that contains the scores that the search returns.
- [var timeScope: GKLeaderboard.TimeScope](./timescope-swift.property.md)
  A filter that restricts the search to scores within a specific period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/playerscope-swift.property)*