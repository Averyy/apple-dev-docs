# init(identifier:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Initializes an achievement for the local player.

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
init(identifier: String)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier;
```

## Mentions

- [Rewarding players with achievements](../rewarding-players-with-achievements.md)

## Return Value

An achievement for a player, or `nil` if an error occurs.

## Discussion

Before creating an achievement, use the [`loadAchievements(completionHandler:)`](./loadachievements%28completionhandler%29.md) method to load the achievements that are in progress. If the achievement you want to report progress on isn’t in the array that GameKit passes to the handler, use this method to initialize the achievement.

## Parameters

- `identifier`: The identifier for the achievement that you enter in App Store Connect.

## See Also

### Loading and Initializing Achievements
- [class func loadAchievements(completionHandler: (([GKAchievement]?, (any Error)?) -> Void)?)](./loadachievements%28completionhandler%29.md)
  Loads the achievements that you previously reported the player making progress toward.
- [init(identifier: String, player: GKPlayer)](./init%28identifier,player%29.md)
  Initializes an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/init(identifier:))*