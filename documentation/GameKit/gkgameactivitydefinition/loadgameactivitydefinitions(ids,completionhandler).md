# loadGameActivityDefinitions(IDs:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

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
class func loadGameActivityDefinitions(IDs activityDefinitionIDs: [String]?, completionHandler: @escaping @Sendable ([GKGameActivityDefinition]?, (any Error)?) -> Void)
```

```swift
class func loadGameActivityDefinitions(IDs activityDefinitionIDs: [String]?) async throws -> [GKGameActivityDefinition]
```

```objc
+ (void) loadGameActivityDefinitionsWithIDs:(NSArray<NSString *> *) activityDefinitionIDs completionHandler:(void (^)(NSArray<GKGameActivityDefinition *> *activityDefinitions, NSError *error)) completionHandler;
```

## Mentions

- [Creating activities for your game](../creating-activities-for-your-game.md)

## See Also

### Loading activity definitions
- [class func loadGameActivityDefinitions(completionHandler: ([GKGameActivityDefinition]?, (any Error)?) -> Void)](./loadgameactivitydefinitions%28completionhandler%29.md)
  Loads all the game activity definitions for the current game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/loadgameactivitydefinitions(ids:completionhandler:))*