# start(definition:partyCode:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Creates and starts a new game activity with a custom party code.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func start(definition activityDefinition: GKGameActivityDefinition, partyCode: String) throws -> GKGameActivity
```

```objc
+ (GKGameActivity *) startWithDefinition:(GKGameActivityDefinition *) activityDefinition partyCode:(NSString *) partyCode error:(NSError **) error;
```

## Mentions

- [Creating activities for your game](../creating-activities-for-your-game.md)

## Discussion

The framework converts the party code to uppercase.

## See Also

### Creating an activity
- [init(definition: GKGameActivityDefinition)](./init%28definition%29.md)
  Creates a game activity with definition.
- [class func start(definition: GKGameActivityDefinition) throws -> GKGameActivity](./start%28definition%29.md)
  Creates and starts a game activity with a definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/start(definition:partycode:))*