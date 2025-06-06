# resetAchievements(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Resets the percentage completed for all of the player’s achievements.

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
class func resetAchievements() async throws
```

## Mentions

- [Rewarding players with achievements](rewarding-players-with-achievements.md)

#### Discussion

This method sets the percentage complete for all of the player’s achievements to zero. If you hide an achievement when you create it in App Store Connect, this method hides the achievement again.

## Parameters

- `completionHandler`: The block receives the following parameter:

## See Also

- [class func report([GKAchievement], withCompletionHandler: (((any Error)?) -> Void)?)](gkachievement/report(_:withcompletionhandler:).md)
  Reports the player’s progress of players toward one or more achievements.
- [class func report([GKAchievement], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](gkachievement/report(_:witheligiblechallenges:withcompletionhandler:).md)
  Reports the player’s progress on achievements and limits the challenges, associated with those achievements, that the player may complete.
- [var showsCompletionBanner: Bool](gkachievement/showscompletionbanner.md)
  A Boolean value that indicates whether GameKit displays a banner when the player completes the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/resetachievements(completionhandler:))*