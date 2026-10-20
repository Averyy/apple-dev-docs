# title

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The localized title for the leaderboard.

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
var title: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * title;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * title;
```

## Mentions

- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

## See Also

### Accessing Identifier and Type Properties
- [var baseLeaderboardID: String](./baseleaderboardid.md)
  The ID that Game Center uses to identify this leaderboard.
- [var type: GKLeaderboard.LeaderboardType](./type.md)
  The type of leaderboard, classic or recurring.
- [GKLeaderboard.LeaderboardType](./leaderboardtype.md)
  Specifies whether a leaderboard is recurring.
- [var groupIdentifier: String?](./groupidentifier.md)
  The identifier for the group the leaderboard belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/title)*