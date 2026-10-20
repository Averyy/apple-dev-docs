# loadGameActivityDefinitions(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Loads all the game activity definitions for the current game.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func loadGameActivityDefinitions(completionHandler: @escaping @Sendable ([GKGameActivityDefinition]?, (any Error)?) -> Void)
```

```swift
class var all: [GKGameActivityDefinition] { get async throws }
```

```objc
+ (void) loadGameActivityDefinitionsWithCompletionHandler:(void (^)(NSArray<GKGameActivityDefinition *> *activityDefinitions, NSError *error)) completionHandler;
```

## See Also

### Loading activity definitions
- [class func loadGameActivityDefinitions(IDs: [String]?, completionHandler: ([GKGameActivityDefinition]?, (any Error)?) -> Void)](./loadgameactivitydefinitions%28ids,completionhandler%29.md)
  Loads game activity definitions with the supplied App Store Connect identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/loadgameactivitydefinitions(completionhandler:))*