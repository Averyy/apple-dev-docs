# spotlightQuery(_:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Performs a Spotlight search query for entities of this type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func spotlightQuery(_ userQuery: String? = nil) async throws -> [AnyAppEntity]
```

## Mentions

- [Testing your App Intents code](../testing-your-app-intents-code.md)

## Return Value

An array of `AnyAppEntity` instances that match the search criteria.

## Discussion

> **Throws**: An error if the spotlight query fails.

## Parameters

- `userQuery`: The search query string. If `nil`, returns all indexed entities.

## See Also

### Searching matching entities
- [func entities<Identifier>(identifiers: [Identifier]) async throws -> [AnyAppEntity]](./entities%28identifiers%29.md)
  Retrieves entities by their identifiers.
- [func entityQuery<Identifier>(identifiers: [Identifier]) -> AnyEntityQuery](./entityquery%28identifiers%29.md)
  Creates an entity query that searches for entities by their identifiers.
- [func entities(matching: String) async throws -> [AnyAppEntity]](./entities%28matching%29.md)
  Finds app entities that match a given string query.
- [func entityQuery(matching: String) -> AnyEntityQuery](./entityquery%28matching%29.md)
  Creates an entity query that searches for entities that match a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/spotlightquery(_:))*