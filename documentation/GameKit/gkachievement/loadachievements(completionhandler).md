# loadAchievements(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

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
class func loadAchievements(completionHandler: (@Sendable ([GKAchievement]?, (any Error)?) -> Void)? = nil)
```

```swift
class func loadAchievements() async throws -> [GKAchievement]
```

```objc
+ (void) loadAchievementsWithCompletionHandler:(void (^)(NSArray<GKAchievement *> *achievements, NSError *error)) completionHandler;
```

## Mentions

- [Rewarding players with achievements](../rewarding-players-with-achievements.md)

## Parameters

- `completionHandler`: A block that GameKit calls when this method loads the achievements.

  The block receives the following parameters:

  - **`achievements`**: The achievements that you previously reported progress for the local player.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading and Initializing Achievements
- [init(identifier: String)](./init%28identifier%29.md)
  Initializes an achievement for the local player.
- [init(identifier: String, player: GKPlayer)](./init%28identifier,player%29.md)
  Initializes an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/loadachievements(completionhandler:))*