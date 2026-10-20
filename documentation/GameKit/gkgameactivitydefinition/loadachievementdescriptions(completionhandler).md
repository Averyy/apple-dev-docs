# loadAchievementDescriptions(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads all associated achievements that have defined deep links to this game activity definition.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func loadAchievementDescriptions(completionHandler: @escaping @Sendable ([GKAchievementDescription]?, (any Error)?) -> Void)
```

```swift
var achievementDescriptions: [GKAchievementDescription] { get async throws }
```

```objc
- (void) loadAchievementDescriptionsWithCompletionHandler:(void (^)(NSArray<GKAchievementDescription *> *achievementDescriptions, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/loadachievementdescriptions(completionhandler:))*