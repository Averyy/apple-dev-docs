# loadAchievements(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads the achievements that you previously reported the player making progress toward.

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
class func loadAchievements() async throws -> [GKAchievement]
```

## Mentions

- [Rewarding players with achievements](rewarding-players-with-achievements.md)

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [init(identifier: String)](gkachievement/init(identifier:).md)
  Initializes an achievement for the local player.
- [init(identifier: String, player: GKPlayer)](gkachievement/init(identifier:player:).md)
  Initializes an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/loadachievements(completionhandler:))*