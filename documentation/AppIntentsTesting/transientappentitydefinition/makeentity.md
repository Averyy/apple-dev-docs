# makeEntity

**Framework**: App Intents Testing  
**Kind**: property

Creates a populated instance of this transient entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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