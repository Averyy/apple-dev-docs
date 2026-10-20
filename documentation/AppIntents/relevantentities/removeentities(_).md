# removeEntities(_:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

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

> **Throws**: An error if the removal fails.

## Parameters

- `entities`: The entities to remove from all contexts.

## See Also

### Removing the current donations
- [func removeAllEntities() async throws](./removeallentities%28%29.md)
  Removes all suggested entities across all contexts.
- [func removeAllEntities(for: AppEntityContext) async throws](./removeallentities%28for%29.md)
  Removes all donated entities for the given context.
- [func removeEntities([any AppEntity], from: AppEntityContext) async throws](./removeentities%28_,from%29.md)
  Removes specific entities from the given context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantentities/removeentities(_:))*