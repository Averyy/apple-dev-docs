# EntityQuery

**Framework**: App Intents  
**Kind**: protocol

An interface for locating entities using their identifiers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol EntityQuery : DynamicOptionsProvider, PersistentlyIdentifiable, Sendable
```

## Mentions

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)

#### Overview

The entity query provides the model object in which ways instances of a particular app entity type can be queried by Siri and the Shortcuts app, and implements the retrieval of such instances.

##### Conform to the Entityquery Protocol

In order to allow Siri and Shortcuts to retrieve [`AppEntity`](appentity.md) instances, create a new type conforming to `EntityQuery`.

##### Resolving Entities By Identifier

In some scenarios, Siri or Shortcuts already knows exactly which entity the user is referring to, and needs to retrieve the actual entity instance given its unique identifier.

To support this retrieval method, implement [`entities(for:)`](entityquery/entities(for:).md), which given an array of AppEntity identifiers, returns corresponding entity instances. The method should first lookup if said instance already exists in memory. If the instance doesn’t exist, then `perform` can make asynchronous calls to retrieve the entity (ex: from disk or from a remote back-end). If the entity corresponding to a supplied identifier is not available anymore, then it should be omitted from the returned array.

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
  Returns the initial results shown when a list of options backed by this query is presented.
### Associated Types
- [associatedtype Result = [Self.Entity]](entityquery/result.md)

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
- [UniqueAppEntityQuery](uniqueappentityquery.md)
### Conforming Types
- [UniqueAppEntityProvider](uniqueappentityprovider.md)

## See Also

- [protocol EnumerableEntityQuery](enumerableentityquery.md)
  An interface you use to provide a short list of entities that are relatively small in size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery)*