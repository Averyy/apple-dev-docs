# init(identifier:player:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Initializes an achievement for a player.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(identifier: String, player: GKPlayer)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier player:(GKPlayer *) player;
```

## Mentions

- [Rewarding players with achievements](../rewarding-players-with-achievements.md)

## Return Value

An achievement for a player, or `nil` if an error occurs.

## Discussion

Before creating an achievement, use the [`loadAchievements(completionHandler:)`](./loadachievements%28completionhandler%29.md) method to load the achievements that are in progress. If the achievement you want to report progress on isn’t in the array that GameKit passes to the handler, use this method to initialize the achievement, but only when reporting progress for a participant at the end of a turn-based match. Otherwise, use the [`init(identifier:)`](./init%28identifier%29.md) method to initialize the achievement.

## Parameters

- `identifier`: The identifier for the achievement that you enter in App Store Connect.
- `player`: The player who is earning the achievement.

## See Also

### Loading and Initializing Achievements
- [class func loadAchievements(completionHandler: (([GKAchievement]?, (any Error)?) -> Void)?)](./loadachievements%28completionhandler%29.md)
  Loads the achievements that you previously reported the player making progress toward.
- [init(identifier: String)](./init%28identifier%29.md)
  Initializes an achievement for the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/init(identifier:player:))*