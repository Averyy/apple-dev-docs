# spotlightQuery(_:)

**Framework**: App Intents Testing  
**Kind**: method

Performs a Spotlight search query for entities of this type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func spotlightQuery(_ userQuery: String? = nil) async throws -> [AnyAppEntity]
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Return Value

An array of `AnyAppEntity` instances that match the search criteria.

#### Discussion

> **Note**: An error if the spotlight query fails.

## Parameters

- `userQuery`: The search query string. If `nil`, returns all indexed entities.

## See Also

- [func entities<Identifier>(identifiers: [Identifier]) async throws -> [AnyAppEntity]](appentitydefinition/entities(identifiers:).md)
  Retrieves entities by their identifiers.
- [func entityQuery<Identifier>(identifiers: [Identifier]) -> AnyEntityQuery](appentitydefinition/entityquery(identifiers:).md)
  Creates an entity query that searches for entities by their identifiers.
- [func entities(matching: String) async throws -> [AnyAppEntity]](appentitydefinition/entities(matching:).md)
  Finds app entities that match a given string query.
- [func entityQuery(matching: String) -> AnyEntityQuery](appentitydefinition/entityquery(matching:).md)
  Creates an entity query that searches for entities that match a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/spotlightquery(_:))*