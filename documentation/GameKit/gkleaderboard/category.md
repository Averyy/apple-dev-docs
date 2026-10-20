# category

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The named leaderboard to retrieve information from.

**Availability**:
- iOS 4.1+ - Deprecated in 7.0
- iPadOS 4.1+ - Deprecated in 7.0
- Mac Catalyst 4.1+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`loadEntries(for:timeScope:range:completionHandler:)`](./loadentries%28for,timescope,range,completionhandler%29.md) method instead.

## Declaration

```swift
var category: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * category;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * category;
```

#### Discussion

If non-`nil`, Game Center only returns scores from the matching leaderboard. If `nil`, Game Center searches all previous scores of the game. The default is `nil`.

## See Also

### Deprecated properties
- [var identifier: String?](./identifier.md)
  The named leaderboard to retrieve information from.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the leaderboard object is retrieving scores.
- [var localPlayerScore: GKScore?](./localplayerscore.md)
  The score that the local player earns.
- [var maxRange: Int](./maxrange.md)
  The size of the leaderboard.
- [var playerScope: GKLeaderboard.PlayerScope](./playerscope-swift.property.md)
  A filter that restricts the search to a subset of the players in Game Center.
- [var range: NSRange](./range.md)
  The numerical score rankings to return from the search.
- [var scores: [GKScore]?](./scores.md)
  An array of scores that contains the scores that the search returns.
- [var timeScope: GKLeaderboard.TimeScope](./timescope-swift.property.md)
  A filter that restricts the search to scores within a specific period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/category)*