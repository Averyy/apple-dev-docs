# entityQuery(identifiers:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Creates an entity query that searches for entities by their identifiers.

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
func entityQuery<Identifier>(identifiers: [Identifier]) -> AnyEntityQuery where Identifier : EntityIdentifierConvertible
```

## Return Value

An entity query, configured for identifier-based searching.

## Parameters

- `identifiers`: An array of entity identifiers to search for.

## See Also

### Searching matching entities
- [func entities<Identifier>(identifiers: [Identifier]) async throws -> [AnyAppEntity]](./entities%28identifiers%29.md)
  Retrieves entities by their identifiers.
- [func entities(matching: String) async throws -> [AnyAppEntity]](./entities%28matching%29.md)
  Finds app entities that match a given string query.
- [func entityQuery(matching: String) -> AnyEntityQuery](./entityquery%28matching%29.md)
  Creates an entity query that searches for entities that match a given string.
- [func spotlightQuery(String?) async throws -> [AnyAppEntity]](./spotlightquery%28_%29.md)
  Performs a Spotlight search query for entities of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/entityquery(identifiers:))*