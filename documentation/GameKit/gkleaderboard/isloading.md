# isLoading

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the leaderboard object is retrieving scores.

**Availability**:
- iOS 4.1+ - Deprecated in 14.0
- iPadOS 4.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use the [`loadEntries(for:timeScope:range:completionHandler:)`](./loadentries%28for,timescope,range,completionhandler%29.md) method instead.

## Declaration

```swift
var isLoading: Bool { get }
```

```objc
@property (readonly, getter=isLoading) BOOL loading;
```

## Discussion

The value of the `loading` property is [`true`](../../Swift/true.md) if the leaderboard object has any pending requests for scores.

## See Also

### Deprecated properties
- [var category: String?](./category.md)
  The named leaderboard to retrieve information from.
- [var identifier: String?](./identifier.md)
  The named leaderboard to retrieve information from.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/isloading)*