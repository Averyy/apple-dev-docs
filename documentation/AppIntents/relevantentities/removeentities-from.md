# removeEntities(_:from:)

**Framework**: App Intents  
**Kind**: method

Removes specific entities from the given context.

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
func removeEntities(_ entities: [any AppEntity], from context: AppEntityContext) async throws
```

#### Discussion

> **Note**: An error if the removal fails.

## Parameters

- `entities`: The entities to remove.
- `context`: The context from which to remove the entities.

## See Also

- [func removeAllEntities() async throws](relevantentities/removeallentities.md)
  Removes all suggested entities across all contexts.
- [func removeAllEntities(for: AppEntityContext) async throws](relevantentities/removeallentities(for:).md)
  Removes all donated entities for the given context.
- [func removeEntities([any AppEntity]) async throws](relevantentities/removeentities(_:).md)
  Removes the specified entities across all contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantentities/removeentities(_:from:))*