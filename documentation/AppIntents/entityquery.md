# EntityQuery

**Framework**: App Intents  
**Kind**: protocol

An interface for locating app entity instances by identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol EntityQuery : DynamicOptionsProvider, PersistentlyIdentifiable, Sendable
```

## Mentions

- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

#### Overview

An entity query defines how Apple Intelligence, Siri, and the Shortcuts app retrieve instances of a specific [`AppEntity`](appentity.md) type, and implements the lookup logic. To let Siri and Shortcuts retrieve `AppEntity` instances, create a type that conforms to [`EntityQuery`](entityquery.md).

##### Resolve Entities By Identifier

In some scenarios, Apple Intelligence already knows exactly which entity the person is referring to, and needs to retrieve the actual entity instance given its unique identifier.

To support this retrieval method, implement [`entities(for:)`](entityquery/entities(for:).md), which, given an array of [`AppEntity`](appentity.md) identifiers, returns corresponding entity instances. In your `entities(for:)` implementation, first look up whether the instance already exists in memory. If the instance doesn’t exist, make asynchronous calls — for example, retrieving from disk or a backend service. If the entity for a provided identifier is no longer available, omit it from the returned array.

```swift
struct MyPhotoQuery: EntityQuery {
    func entities(for identifiers: [UUID]) async throws -> [MyPhoto] {
        myPhotoStore.filter { identifiers.contains($0.id) }
    }
}
```

## Topics

### Creating a query
- [init()](entityquery/init.md)
### Searching for entities
- [func entities(for: [Self.Entity.ID]) async throws -> [Self.Entity]](entityquery/entities(for:).md)
  Retrieves instances by identifier.
- [associatedtype Entity : AppEntity = Self.Result.Result.ValueType](entityquery/entity.md)
  The entity type that this query knows how to resolve.
### Suggesting entities
- [func suggestedEntities() async throws -> Self.Result](entityquery/suggestedentities.md)
  Returns the initial results to display when the system presents options backed by this query.
### Associated Types
- [associatedtype Result = [Self.Entity]](entityquery/result.md)
### Instance Methods
- [func displayRepresentations(for: [Self.Entity.ID], requestedComponents: DisplayRepresentation.Components) async throws -> [Self.Entity.ID : DisplayRepresentation]](entityquery/displayrepresentations(for:requestedcomponents:).md)
  Returns a list of display representation values by identifier based on the requested components.
### Type Aliases
- [EntityQuery.ExecutionTargets](entityquery/executiontargets.md)
### Type Properties
- [static var allowedExecutionTargets: IntentExecutionTargets](entityquery/allowedexecutiontargets.md)
  A set of targets that can run this query.

## Relationships

### Inherits From
- [DynamicOptionsProvider](dynamicoptionsprovider.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [EntityPropertyQuery](entitypropertyquery.md)
- [EntityStringQuery](entitystringquery.md)
- [EnumerableEntityQuery](enumerableentityquery.md)
- [IndexedEntityQuery](indexedentityquery.md)
- [UniqueAppEntityQuery](uniqueappentityquery.md)
### Conforming Types
- [UniqueAppEntityProvider](uniqueappentityprovider.md)

## See Also

- [protocol IndexedEntityQuery](indexedentityquery.md)
  An interface that adds Spotlight reindexing support to your entity query.
- [protocol EnumerableEntityQuery](enumerableentityquery.md)
  An interface you use to provide a short list of entities that are relatively small in size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery)*