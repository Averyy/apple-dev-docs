# removeAllEntities(for:)

**Framework**: App Intents  
**Kind**: method

Removes all donated entities for the given context.

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
func removeAllEntities(for context: AppEntityContext) async throws
```

#### Discussion

> **Note**: An error if the removal fails.

## Parameters

- `context`: The context whose donated entities should be removed.

## See Also

- [func removeAllEntities() async throws](relevantentities/removeallentities.md)
  Removes all suggested entities across all contexts.
- [func removeEntities([any AppEntity]) async throws](relevantentities/removeentities(_:).md)
  Removes the specified entities across all contexts.
- [func removeEntities([any AppEntity], from: AppEntityContext) async throws](relevantentities/removeentities(_:from:).md)
  Removes specific entities from the given context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantentities/removeallentities(for:))*