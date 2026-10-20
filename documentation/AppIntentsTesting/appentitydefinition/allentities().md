# allEntities()

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Fetches all available entities of this type.

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
func allEntities() async throws -> [AnyAppEntity]
```

#### Return Value

An array containing all entities of this type.

#### Discussion

> **Throws**: Any errors encountered during the query execution.

## See Also

### Retrieving all entities
- [func allEntitiesQuery() -> AnyEntityQuery](./allentitiesquery%28%29.md)
  Creates an entity query that retrieves all available entities of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/allentities())*