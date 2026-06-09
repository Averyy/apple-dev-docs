# init(entities:)

**Framework**: App Intents  
**Kind**: init

Creates a new entity identifier collection from entities.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(entities: [Entity])
```

#### Discussion

This initializer adds the identifier for each entity to the collection and caches the entity instances for fast retrieval later.

## Parameters

- `entities`: The entities to add to the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitycollection/init(entities:))*