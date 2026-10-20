# AppEntityDefinition

**Framework**: App Intents Testing  
**Kind**: struct  
**Role**: Structure

A definition you use to dynamically create entity instances for testing.

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
struct AppEntityDefinition
```

## Mentions

- [Testing your App Intents code](./testing-your-app-intents-code.md)

#### Overview

To create an app entity instance for testing, load the definition for your app entity, using [`IntentDefinitions`](./intentdefinitions.md) and its [`entities`](./intentdefinitions/entities.md) property, then create an entity instance as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let landmarkEntity = definitions.entities[
    "LandmarkEntity"
]
let entity = landmarkEntity.makeReference(
    identifier: "yosemite-falls"
)
```

## Topics

### Creating an app entity instance
- [func makeReference(identifier: String) -> AnyAppEntity](./appentitydefinition/makereference%28identifier%29.md)
  Creates an app entity instance of the given entity type.
### Retrieving all entities
- [func allEntities() async throws -> [AnyAppEntity]](./appentitydefinition/allentities%28%29.md)
  Fetches all available entities of this type.
- [func allEntitiesQuery() -> AnyEntityQuery](./appentitydefinition/allentitiesquery%28%29.md)
  Creates an entity query that retrieves all available entities of this type.
### Searching matching entities
- [func entities<Identifier>(identifiers: [Identifier]) async throws -> [AnyAppEntity]](./appentitydefinition/entities%28identifiers%29.md)
  Retrieves entities by their identifiers.
- [func entityQuery<Identifier>(identifiers: [Identifier]) -> AnyEntityQuery](./appentitydefinition/entityquery%28identifiers%29.md)
  Creates an entity query that searches for entities by their identifiers.
- [func entities(matching: String) async throws -> [AnyAppEntity]](./appentitydefinition/entities%28matching%29.md)
  Finds app entities that match a given string query.
- [func entityQuery(matching: String) -> AnyEntityQuery](./appentitydefinition/entityquery%28matching%29.md)
  Creates an entity query that searches for entities that match a given string.
- [func spotlightQuery(String?) async throws -> [AnyAppEntity]](./appentitydefinition/spotlightquery%28_%29.md)
  Performs a Spotlight search query for entities of this type.
### Accessing suggested entities
- [func suggestedEntities() async throws -> [AnyAppEntity]](./appentitydefinition/suggestedentities%28%29.md)
  Fetches all suggested entities of this type.
- [func suggestedEntitiesQuery() -> AnyEntityQuery](./appentitydefinition/suggestedentitiesquery%28%29.md)
  Creates an entity query that retrieves suggested entities of this type.
### Accessing onscreen entities
- [func viewAnnotations() async throws -> [ViewAnnotation]](./appentitydefinition/viewannotations%28%29.md)
  Provides the currently visible onscreen entities.
### Identifying the entity
- [let typeIdentifier: String](./appentitydefinition/typeidentifier.md)
  The entity type’s unique identifier.
- [let bundleIdentifier: String](./appentitydefinition/bundleidentifier.md)
  The bundle identifier of the app that includes the app entity.
### Instance Methods
- [func resolved(from: IntentFile) async throws -> AnyAppEntity](./appentitydefinition/resolved%28from%29-2fld0.md)
  Resolves an entity from an exported intent file through the entity type’s transferable conformance.
- [func resolved<T>(from: T) async throws -> AnyAppEntity](./appentitydefinition/resolved%28from%29-4yp5n.md)
  Resolves an entity from a system intent value type through the entity type’s transferable conformance.
- [func resolved<T>(from: T) async throws -> AnyAppEntity](./appentitydefinition/resolved%28from%29-7c04a.md)
  Resolves an entity from a transferable intent value type through the entity type’s transferable conformance.
### Default Implementations
- [AppIntentTypeDefinition Implementations](./appentitydefinition/appintenttypedefinition-implementations.md)

## Relationships

### Conforms To
- [AppIntentTypeDefinition](./appintenttypedefinition.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing app entities and queries
- [var entities: IntentDefinitions.DefinitionCollection<AppEntityDefinition>](./intentdefinitions/entities.md)
  The definitions for the target app’s app entities.
- [var valueQueries: IntentDefinitions.DefinitionCollection<IntentValueQueryDefinition>](./intentdefinitions/valuequeries.md)
  The definitions for the app’s intent value queries.
- [struct IntentValueQueryDefinition](./intentvaluequerydefinition.md)
  A definition you use to create an intent value query for testing.
- [var transientEntities: IntentDefinitions.DefinitionCollection<TransientAppEntityDefinition>](./intentdefinitions/transiententities.md)
  Retrieve a transient app entity definition using subscript syntax.
- [struct TransientAppEntityDefinition](./transientappentitydefinition.md)
  A definition you use to dynamically create transient app entities for testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition)*