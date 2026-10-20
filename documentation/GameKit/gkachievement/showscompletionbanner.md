# showsCompletionBanner

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign) BOOL showsCompletionBanner;
```

*macOS*

```objc
@property (atomic, assign) BOOL showsCompletionBanner;
```

## Mentions

- [Rewarding players with achievements](../rewarding-players-with-achievements.md)

#### Discussion

If this property is [`true`](../../Swift/true.md), GameKit displays a notification banner to inform the player that they completed the achievement. If you want to present your own interface, set this property to [`false`](../../Swift/false.md). The default value is [`true`](../../Swift/true.md).

## See Also

### Reporting Progress on Achievements
- [class func report([GKAchievement], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,withcompletionhandler%29.md)
  Reports the player’s progress of players toward one or more achievements.
- [class func report([GKAchievement], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,witheligiblechallenges,withcompletionhandler%29.md)
  Reports the player’s progress on achievements and limits the challenges, associated with those achievements, that the player may complete.
- [class func resetAchievements(completionHandler: (((any Error)?) -> Void)?)](./resetachievements%28completionhandler%29.md)
  Resets the percentage completed for all of the player’s achievements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/showscompletionbanner)*