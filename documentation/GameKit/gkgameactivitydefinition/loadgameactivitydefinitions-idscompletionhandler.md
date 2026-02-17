# loadGameActivityDefinitions(IDs:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads game activity definitions with the supplied App Store Connect identifiers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func loadGameActivityDefinitions(IDs activityDefinitionIDs: [String]?) async throws -> [GKGameActivityDefinition]
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

## See Also

- [class func loadGameActivityDefinitions(completionHandler: ([GKGameActivityDefinition]?, (any Error)?) -> Void)](gkgameactivitydefinition/loadgameactivitydefinitions(completionhandler:).md)
  Loads all the game activity definitions for the current game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/loadgameactivitydefinitions(ids:completionhandler:))*