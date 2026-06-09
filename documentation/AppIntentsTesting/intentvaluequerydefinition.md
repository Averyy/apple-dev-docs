# IntentValueQueryDefinition

**Framework**: App Intents Testing  
**Kind**: struct

A definition you use to create an intent value query for testing.

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
struct IntentValueQueryDefinition
```

#### Overview

To create an intent value for testing and verify its results, first get its definition using [`IntentDefinitions`](intentdefinitions.md) and its [`valueQueries`](intentdefinitions/valuequeries.md) property. Then, perform the query and verify that it returns the expected results as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let searchQuery = definitions.valueQueries[
    "LandmarkIntentValueQuery"
]

let result = try await searchQuery.values(for: "Arizona")

// Code to verify the query's results.
// ...
```

## Topics

### Performing the intent value query
- [func values(for: some IntentValueConvertible) async throws -> ResolvedValueQueryResult](intentvaluequerydefinition/values(for:).md)
  Performs the value query with the given input and returns matching results.
### Identifying the query
- [let bundleIdentifier: String](intentvaluequerydefinition/bundleidentifier.md)
  The bundle identifier of the app that includes the query.
- [let queryIdentifier: String](intentvaluequerydefinition/queryidentifier.md)
  The query’s unique identifier.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var entities: IntentDefinitions.DefinitionCollection<AppEntityDefinition>](intentdefinitions/entities.md)
  The definitions for the target app’s app entities.
- [struct AppEntityDefinition](appentitydefinition.md)
  A definition you use to dynamically create entity instances for testing.
- [var valueQueries: IntentDefinitions.DefinitionCollection<IntentValueQueryDefinition>](intentdefinitions/valuequeries.md)
  The definitions for the app’s intent value queries.
- [var transientEntities: IntentDefinitions.DefinitionCollection<TransientAppEntityDefinition>](intentdefinitions/transiententities.md)
  Retrieve a transient app entity definition using subscript syntax.
- [struct TransientAppEntityDefinition](transientappentitydefinition.md)
  A definition you use to dynamically create transient app entities for testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvaluequerydefinition)*