# entities(identifiers:)

**Framework**: App Intents Testing  
**Kind**: method

Retrieves entities by their identifiers.

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
func entities<Identifier>(identifiers: [Identifier]) async throws -> [AnyAppEntity] where Identifier : EntityIdentifierConvertible
```

#### Return Value

An array of entities matching the provided identifiers.

#### Discussion

> **Note**: Any errors encountered during the query execution.

## Parameters

- `identifiers`: An array of entity identifiers to look up.

## See Also

- [func entityQuery<Identifier>(identifiers: [Identifier]) -> AnyEntityQuery](appentitydefinition/entityquery(identifiers:).md)
  Creates an entity query that searches for entities by their identifiers.
- [func entities(matching: String) async throws -> [AnyAppEntity]](appentitydefinition/entities(matching:).md)
  Finds app entities that match a given string query.
- [func entityQuery(matching: String) -> AnyEntityQuery](appentitydefinition/entityquery(matching:).md)
  Creates an entity query that searches for entities that match a given string.
- [func spotlightQuery(String?) async throws -> [AnyAppEntity]](appentitydefinition/spotlightquery(_:).md)
  Performs a Spotlight search query for entities of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/entities(identifiers:))*