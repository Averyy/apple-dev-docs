# showsCompletionBanner

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether GameKit displays a banner when the player completes the achievement.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var showsCompletionBanner: Bool { get set }
```

## Mentions

- [Rewarding players with achievements](rewarding-players-with-achievements.md)

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), GameKit displays a notification banner to inform the player that they completed the achievement. If you want to present your own interface, set this property to [`false`](https://developer.apple.com/documentation/swift/false). The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [class func report([GKAchievement], withCompletionHandler: (((any Error)?) -> Void)?)](gkachievement/report(_:withcompletionhandler:).md)
  Reports the player’s progress of players toward one or more achievements.
- [class func report([GKAchievement], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](gkachievement/report(_:witheligiblechallenges:withcompletionhandler:).md)
  Reports the player’s progress on achievements and limits the challenges, associated with those achievements, that the player may complete.
- [class func resetAchievements(completionHandler: (((any Error)?) -> Void)?)](gkachievement/resetachievements(completionhandler:).md)
  Resets the percentage completed for all of the player’s achievements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/showscompletionbanner)*