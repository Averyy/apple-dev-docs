# TransientAppEntityDefinition

**Framework**: App Intents Testing  
**Kind**: struct

A definition you use to dynamically create transient app entities for testing.

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
struct TransientAppEntityDefinition
```

#### Overview

To create a transient app entity instance for testing, load the definition for your transient app entity using [`IntentDefinitions`](intentdefinitions.md) and its [`transientEntities`](intentdefinitions/transiententities.md) property, then create an entity instance as shown in the following example:

```swift
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let sessionEntity = definitions.transientEntities[
    "UserSessionEntity"
]
let entity = sessionEntity.makeEntity(
    sessionId: "temp-session-123",
    startTime: Date()
)
```

## Topics

### Creating a transient entity instance
- [var makeEntity: IntentValuePropertiesCallable<AnyTransientAppEntity>](transientappentitydefinition/makeentity.md)
  Creates a populated instance of this transient entity.
### Identifying the entity
- [let bundleIdentifier: String](transientappentitydefinition/bundleidentifier.md)
  The bundle identifier of the app that contains this entity.
- [let typeIdentifier: String](transientappentitydefinition/typeidentifier.md)
  The entity type’s identifier.
### Instance Methods
- [func resolved<T>(from: T) async throws -> AnyTransientAppEntity](transientappentitydefinition/resolved(from:)-1lap2.md)
  Resolves a transient entity from a transferable intent value type through the entity type’s `Transferable` conformance.
- [func resolved<T>(from: T) async throws -> AnyTransientAppEntity](transientappentitydefinition/resolved(from:)-3jjpx.md)
  Resolves a transient entity from a system intent value type through the entity type’s `Transferable` conformance.
- [func resolved(from: IntentFile) async throws -> AnyTransientAppEntity](transientappentitydefinition/resolved(from:)-6xsjl.md)
  Resolves a transient entity from an exported `IntentFile` through the entity type’s `Transferable` conformance.
### Default Implementations
- [AppIntentTypeDefinition Implementations](transientappentitydefinition/appintenttypedefinition-implementations.md)

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
- [struct AppEntityDefinition](appentitydefinition.md)
  A definition you use to dynamically create entity instances for testing.
- [var valueQueries: IntentDefinitions.DefinitionCollection<IntentValueQueryDefinition>](intentdefinitions/valuequeries.md)
  The definitions for the app’s intent value queries.
- [struct IntentValueQueryDefinition](intentvaluequerydefinition.md)
  A definition you use to create an intent value query for testing.
- [var transientEntities: IntentDefinitions.DefinitionCollection<TransientAppEntityDefinition>](intentdefinitions/transiententities.md)
  Retrieve a transient app entity definition using subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/transientappentitydefinition)*