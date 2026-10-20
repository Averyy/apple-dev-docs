# init(definition:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Creates a game activity with definition.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(definition activityDefinition: GKGameActivityDefinition)
```

```objc
- (instancetype) initWithDefinition:(GKGameActivityDefinition *) activityDefinition;
```

## See Also

### Creating an activity
- [class func start(definition: GKGameActivityDefinition) throws -> GKGameActivity](./start%28definition%29.md)
  Creates and starts a game activity with a definition.
- [class func start(definition: GKGameActivityDefinition, partyCode: String) throws -> GKGameActivity](./start%28definition,partycode%29.md)
  Creates and starts a new game activity with a custom party code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/init(definition:))*