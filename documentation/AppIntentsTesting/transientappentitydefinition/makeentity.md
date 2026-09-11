# makeEntity

**Framework**: App Intents Testing  
**Kind**: property

Creates a populated instance of this transient entity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var makeEntity: IntentValuePropertiesCallable<AnyTransientAppEntity> { get }
```

#### Discussion

```swift
let entityDefinition: TransientAppEntityDefinition = definitions.transientEntities["SomeEntityName"]

let entity = entityDefinition.makeEntity(
    sessionId: "temp-session-123",
    startTime: Date()
)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/transientappentitydefinition/makeentity)*