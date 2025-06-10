# start(definition:partyCode:)

**Framework**: GameKit  
**Kind**: method

Creates and starts a new game activity with a custom party code.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class func start(definition activityDefinition: GKGameActivityDefinition, partyCode: String) throws -> GKGameActivity
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

#### Discussion

The party code will be converted to uppercased.

## See Also

- [init(definition: GKGameActivityDefinition)](gkgameactivity/init(definition:).md)
  Initializes a game activity with definition.
- [class func start(definition: GKGameActivityDefinition) throws -> GKGameActivity](gkgameactivity/start(definition:).md)
  Initializes and starts a game activity with definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/start(definition:partycode:))*