# baseLeaderboardID

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The ID that Game Center uses to identify this leaderboard.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var baseLeaderboardID: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * baseLeaderboardID;
```

## Discussion

This is the same ID that App Store Connect uses to identify this leaderboard.

## See Also

### Accessing Identifier and Type Properties
- [var title: String?](./title.md)
  The localized title for the leaderboard.
- [var type: GKLeaderboard.LeaderboardType](./type.md)
  The type of leaderboard, classic or recurring.
- [GKLeaderboard.LeaderboardType](./leaderboardtype.md)
  Specifies whether a leaderboard is recurring.
- [var groupIdentifier: String?](./groupidentifier.md)
  The identifier for the group the leaderboard belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/baseleaderboardid)*