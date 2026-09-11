# removeAllEntities()

**Framework**: App Intents  
**Kind**: method

Removes all suggested entities across all contexts.

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
func removeAllEntities() async throws
```

#### Discussion

> **Note**: An error if the removal fails.

## See Also

- [func removeAllEntities(for: AppEntityContext) async throws](relevantentities/removeallentities(for:).md)
  Removes all donated entities for the given context.
- [func removeEntities([any AppEntity]) async throws](relevantentities/removeentities(_:).md)
  Removes the specified entities across all contexts.
- [func removeEntities([any AppEntity], from: AppEntityContext) async throws](relevantentities/removeentities(_:from:).md)
  Removes specific entities from the given context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantentities/removeallentities())*