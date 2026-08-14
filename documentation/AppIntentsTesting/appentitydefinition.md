# AppEntityDefinition

**Framework**: App Intents Testing  
**Kind**: struct

A definition you use to dynamically create entity instances for testing.

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
struct AppEntityDefinition
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Overview

To create an app entity instance for testing, load the definition for your app entity, using [`IntentDefinitions`](intentdefinitions.md) and its [`entities`](intentdefinitions/entities.md) property, then create an entity instance as shown in the following example:

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
- [func makeReference(identifier: String) -> AnyAppEntity](appentitydefinition/makereference(identifier:).md)
  Creates an app entity instance of the given entity type.
### Retrieving all entities
- [func allEntities() async throws -> [AnyAppEntity]](appentitydefinition/allentities.md)
  Fetches all available entities of this type.
- [func allEntitiesQuery() -> AnyEntityQuery](appentitydefinition/allentitiesquery.md)
  Creates an entity query that retrieves all available entities of this type.
### Searching matching entities
- [func entities<Identifier>(identifiers: [Identifier]) async throws -> [AnyAppEntity]](appentitydefinition/entities(identifiers:).md)
  Retrieves entities by their identifiers.
- [func entityQuery<Identifier>(identifiers: [Identifier]) -> AnyEntityQuery](appentitydefinition/entityquery(identifiers:).md)
  Creates an entity query that searches for entities by their identifiers.
- [func entities(matching: String) async throws -> [AnyAppEntity]](appentitydefinition/entities(matching:).md)
  Finds app entities that match a given string query.
- [func entityQuery(matching: String) -> AnyEntityQuery](appentitydefinition/entityquery(matching:).md)
  Creates an entity query that searches for entities that match a given string.
- [func spotlightQuery(String?) async throws -> [AnyAppEntity]](appentitydefinition/spotlightquery(_:).md)
  Performs a Spotlight search query for entities of this type.
### Accessing suggested entities
- [func suggestedEntities() async throws -> [AnyAppEntity]](appentitydefinition/suggestedentities.md)
  Fetches all suggested entities of this type.
- [func suggestedEntitiesQuery() -> AnyEntityQuery](appentitydefinition/suggestedentitiesquery.md)
  Creates an entity query that retrieves suggested entities of this type.
### Accessing onscreen entities
- [func viewAnnotations() async throws -> [ViewAnnotation]](appentitydefinition/viewannotations.md)
  Provides the currently visible onscreen entities.
### Identifying the entity
- [let typeIdentifier: String](appentitydefinition/typeidentifier.md)
  The entity type’s unique identifier.
- [let bundleIdentifier: String](appentitydefinition/bundleidentifier.md)
  The bundle identifier of the app that includes the app entity.
### Instance Methods
- [func resolved(from: IntentFile) async throws -> AnyAppEntity](appentitydefinition/resolved(from:)-2fld0.md)
  Resolves an entity from an exported intent file through the entity type’s transferable conformance.
- [func resolved<T>(from: T) async throws -> AnyAppEntity](appentitydefinition/resolved(from:)-4yp5n.md)
  Resolves an entity from a system intent value type through the entity type’s transferable conformance.
- [func resolved<T>(from: T) async throws -> AnyAppEntity](appentitydefinition/resolved(from:)-7c04a.md)
  Resolves an entity from a transferable intent value type through the entity type’s transferable conformance.
### Default Implementations
- [AppIntentTypeDefinition Implementations](appentitydefinition/appintenttypedefinition-implementations.md)

## Relationships

### Conforms To
- [AppIntentTypeDefinition](appintenttypedefinition.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var entities: IntentDefinitions.DefinitionCollection<AppEntityDefinition>](intentdefinitions/entities.md)
  The definitions for the target app’s app entities.
- [var valueQueries: IntentDefinitions.DefinitionCollection<IntentValueQueryDefinition>](intentdefinitions/valuequeries.md)
  The definitions for the app’s intent value queries.
- [struct IntentValueQueryDefinition](intentvaluequerydefinition.md)
  A definition you use to create an intent value query for testing.
- [var transientEntities: IntentDefinitions.DefinitionCollection<TransientAppEntityDefinition>](intentdefinitions/transiententities.md)
  Retrieve a transient app entity definition using subscript syntax.
- [struct TransientAppEntityDefinition](transientappentitydefinition.md)
  A definition you use to dynamically create transient app entities for testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition)*