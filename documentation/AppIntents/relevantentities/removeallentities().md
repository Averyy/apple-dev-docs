# removeAllEntities()

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

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

> **Throws**: An error if the removal fails.

## See Also

### Removing the current donations
- [func removeAllEntities(for: AppEntityContext) async throws](./removeallentities%28for%29.md)
  Removes all donated entities for the given context.
- [func removeEntities([any AppEntity]) async throws](./removeentities%28_%29.md)
  Removes the specified entities across all contexts.
- [func removeEntities([any AppEntity], from: AppEntityContext) async throws](./removeentities%28_,from%29.md)
  Removes specific entities from the given context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantentities/removeallentities())*