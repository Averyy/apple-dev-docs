# removeEntities(_:)

**Framework**: App Intents  
**Kind**: method

Removes the specified entities across all contexts.

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
func removeEntities(_ entities: [any AppEntity]) async throws
```

#### Discussion

> **Note**: An error if the removal fails.

## Parameters

- `entities`: The entities to remove from all contexts.

## See Also

- [func removeAllEntities() async throws](relevantentities/removeallentities.md)
  Removes all suggested entities across all contexts.
- [func removeAllEntities(for: AppEntityContext) async throws](relevantentities/removeallentities(for:).md)
  Removes all donated entities for the given context.
- [func removeEntities([any AppEntity], from: AppEntityContext) async throws](relevantentities/removeentities(_:from:).md)
  Removes specific entities from the given context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantentities/removeentities(_:))*