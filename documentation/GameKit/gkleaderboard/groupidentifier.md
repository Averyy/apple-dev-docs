# groupIdentifier

**Framework**: GameKit  
**Kind**: property

The identifier for the group the leaderboard belongs to.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var groupIdentifier: String? { get }
```

#### Discussion

If you add the leaderboard to a group in App Store Connect, this property is the leaderboard group ID you enter in App Store Connect.

## See Also

- [var baseLeaderboardID: String](gkleaderboard/baseleaderboardid.md)
  The ID that Game Center uses to identify this leaderboard.
- [var title: String?](gkleaderboard/title.md)
  The localized title for the leaderboard.
- [var type: GKLeaderboard.LeaderboardType](gkleaderboard/type.md)
  The type of leaderboard, classic or recurring.
- [GKLeaderboard.LeaderboardType](gkleaderboard/leaderboardtype.md)
  Specifies whether a leaderboard is recurring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/groupidentifier)*