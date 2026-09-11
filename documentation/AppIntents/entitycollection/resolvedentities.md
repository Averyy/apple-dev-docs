# resolvedEntities()

**Framework**: App Intents  
**Kind**: method

Retrieves and returns the entity instances for each identifier in the collection.

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
func resolvedEntities() async throws -> [Entity]
```

#### Return Value

An array of resolved entities.

#### Discussion

> **Note**: An error if the entities cannot be resolved.

Use this method to retrieve the [`AppEntity`](appentity.md) instances for each identifier in the collection. You might use this method in your [`perform()`](appintent/perform().md) method when you need additional data from each entity. If the collection already has a cached set of entity instances, the method returns them. If there are no cached values, the method uses entity queries to request them from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitycollection/resolvedentities())*