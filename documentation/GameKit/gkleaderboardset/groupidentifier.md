# groupIdentifier

**Framework**: GameKit  
**Kind**: property

The identifier for the group that the leaderboard set belongs to.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var groupIdentifier: String? { get }
```

#### Discussion

GameKit sets this property when the leaderboard set is part of a game group, and it calls `loadLeaderboardSetsWithCompletionHandler:` for leaderboards that support game groups.

## See Also

- [var title: String](gkleaderboardset/title.md)
  The localized title for the leaderboard set.
- [var identifier: String?](gkleaderboardset/identifier.md)
  The identifier for the leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset/groupidentifier)*