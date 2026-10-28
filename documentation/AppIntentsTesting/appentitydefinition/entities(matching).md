# entities(matching:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Finds app entities that match a given string query.

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
func entities(matching string: String) async throws -> [AnyAppEntity]
```

## Mentions

- [Testing your App Intents code](../testing-your-app-intents-code.md)

## Return Value

An array of entities that match the search criteria.

## Discussion

> **Throws**: Any errors encountered during the query execution.

## Parameters

- `string`: The search string to match against entity properties.

## See Also

### Searching matching entities
- [func entities<Identifier>(identifiers: [Identifier]) async throws -> [AnyAppEntity]](./entities%28identifiers%29.md)
  Retrieves entities by their identifiers.
- [func entityQuery<Identifier>(identifiers: [Identifier]) -> AnyEntityQuery](./entityquery%28identifiers%29.md)
  Creates an entity query that searches for entities by their identifiers.
- [func entityQuery(matching: String) -> AnyEntityQuery](./entityquery%28matching%29.md)
  Creates an entity query that searches for entities that match a given string.
- [func spotlightQuery(String?) async throws -> [AnyAppEntity]](./spotlightquery%28_%29.md)
  Performs a Spotlight search query for entities of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/entities(matching:))*