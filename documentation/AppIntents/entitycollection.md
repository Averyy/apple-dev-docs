# EntityCollection

**Framework**: App Intents  
**Kind**: struct

An array of entity identifiers that you use to improve the efficiency of operations involving large numbers of entities.

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
struct EntityCollection<Entity> where Entity : AppEntity
```

## Mentions

- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)
- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)

#### Overview

Use an `EntityCollection` type to manage large numbers of entities in an app intent or app entity. An entity collection stores the identifier for each entity initially and provides an option to fetch the entire [`AppEntity`](appentity.md) instances later if needed. Storing only the identifiers initially can save memory and speed up operations that don’t require the entire entity instance.

If you need to store the identifiers for multiple entities, use `EntityCollection` as the type of your variable. If you use an `EntityCollection` for a parameter in an app intent, the system doesn’t force the resolution of each identifier to the full [`AppEntity`](appentity.md) instance during parameter resolution. For a parameter that contains hundreds of entities, not resolving each identifier can save time and memory at a potentially critical moment.

The following example shows the use of an `EntityCollection` in an app intent to disable multiple alarms. Because the code to disable the alarms requires only the identifier for each entity, the type stores those values using an entity collection.

```swift
struct DisableAlarmsIntent: AppIntent {
    static var title: LocalizedStringResource = "Disable Alarms"

    @Parameter(title: "Alarms")
    var alarms: EntityCollection<AlarmEntity>

    func perform() async throws -> some IntentResult {
        // Use the identifiers in the database query without hydration.
        try await AlarmService.disable(alarms.identifiers)

        return .result()
    }
}
```

When you need more than just entity identifiers, you can call [`resolvedEntities()`](entitycollection/resolvedentities().md) to generate the [`AppEntity`](appentity.md) instances for each identifier. The method uses your app’s query types to find or create the corresponding entity instances. After retrieving the entities, the entity collection caches those instances for future access.

## Topics

### Initializers
- [init(entities: [Entity])](entitycollection/init(entities:).md)
  Creates a new entity identifier collection from entities.
- [init(identifiers: [Entity.ID])](entitycollection/init(identifiers:).md)
  Creates a new entity identifier collection.
### Instance Properties
- [var count: Int](entitycollection/count.md)
  The number of entity identifiers in this collection.
- [var identifiers: [Entity.ID]](entitycollection/identifiers.md)
  The entity identifiers in the collection.
- [var isEmpty: Bool](entitycollection/isempty.md)
  A Boolean value that indicates whether the collection is empty.
### Instance Methods
- [func append(Entity.ID)](entitycollection/append(_:)-4ze6w.md)
  Adds the specified entity identifier to the collection.
- [func append(Entity)](entitycollection/append(_:)-yr1u.md)
  Adds the identifier for the specified entity to the collection.
- [func append(contentsOf: [Entity])](entitycollection/append(contentsof:)-7zah3.md)
  Adds the identifiers for multiple entities to the collection.
- [func append(contentsOf: [Entity.ID])](entitycollection/append(contentsof:)-8uhpu.md)
  Adds multiple entity identifiers to the collection.
- [func contains(Entity.ID) -> Bool](entitycollection/contains(_:)-i6hb.md)
  Returns a Boolean value that indicates whether the collection contains the specified entity identifier.
- [func contains(Entity) -> Bool](entitycollection/contains(_:)-u9sl.md)
  Returns a Boolean value that indicates whether the collection contains the identifier for the specified entity.
- [func remove(Entity)](entitycollection/remove(_:)-88jpq.md)
  Removes an entity’s identifier from the collection.
- [func remove(Entity.ID)](entitycollection/remove(_:)-etqg.md)
  Removes the specified entity identifier from the collection.
- [func resolvedEntities() async throws -> [Entity]](entitycollection/resolvedentities.md)
  Retrieves and returns the entity instances for each identifier in the collection.
### Type Aliases
- [EntityCollection.Specification](entitycollection/specification.md)
- [EntityCollection.UnwrappedType](entitycollection/unwrappedtype.md)
- [EntityCollection.ValueType](entitycollection/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](entitycollection/defaultresolverspecification.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitycollection)*