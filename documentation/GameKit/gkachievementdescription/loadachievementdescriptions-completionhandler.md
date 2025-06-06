# loadAchievementDescriptions(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Downloads the localized descriptions of achievements from Game Center.

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
class func loadAchievementDescriptions() async throws -> [GKAchievementDescription]
```

## Mentions

- [Rewarding players with achievements](rewarding-players-with-achievements.md)

#### Discussion

To load the artwork for an achievement, use the [`loadImage(completionHandler:)`](gkachievementdescription/loadimage(completionhandler:).md) method after using this method.

## Parameters

- `completionHandler`: The block receives the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/loadachievementdescriptions(completionhandler:))*