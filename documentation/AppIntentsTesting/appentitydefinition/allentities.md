# allEntities()

**Framework**: App Intents Testing  
**Kind**: method

Fetches all available entities of this type.

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
func allEntities() async throws -> [AnyAppEntity]
```

#### Return Value

An array containing all entities of this type.

#### Discussion

> **Note**: Any errors encountered during the query execution.

## See Also

- [func allEntitiesQuery() -> AnyEntityQuery](appentitydefinition/allentitiesquery.md)
  Creates an entity query that retrieves all available entities of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/allentities())*