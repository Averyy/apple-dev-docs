# UniqueAppEntityProvider

**Framework**: App Intents  
**Kind**: struct

A simplified query type conforming to `UniqueAppEntityQuery`.  Use this as the value of the `defaultQuery` of an entity conforming to `UniqueAppEntity`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct UniqueAppEntityProvider<Entity> where Entity : UniqueAppEntity
```

## Topics

### Initializers
- [init()](uniqueappentityprovider/init.md)
- [init(() async throws -> Entity)](uniqueappentityprovider/init(_:).md)
### Instance Methods
- [func uniqueEntity() async throws -> Entity](uniqueappentityprovider/uniqueentity.md)
### Type Aliases
- [UniqueAppEntityProvider.DefaultValue](uniqueappentityprovider/defaultvalue.md)
- [UniqueAppEntityProvider.Result](uniqueappentityprovider/result.md)
- [UniqueAppEntityProvider.Unique](uniqueappentityprovider/unique.md)
### Default Implementations
- [DynamicOptionsProvider Implementations](uniqueappentityprovider/dynamicoptionsprovider-implementations.md)
- [EntityQuery Implementations](uniqueappentityprovider/entityquery-implementations.md)
- [EnumerableEntityQuery Implementations](uniqueappentityprovider/enumerableentityquery-implementations.md)
- [PersistentlyIdentifiable Implementations](uniqueappentityprovider/persistentlyidentifiable-implementations.md)
- [UniqueAppEntityQuery Implementations](uniqueappentityprovider/uniqueappentityquery-implementations.md)

## Relationships

### Conforms To
- [DynamicOptionsProvider](dynamicoptionsprovider.md)
- [EntityQuery](entityquery.md)
- [EnumerableEntityQuery](enumerableentityquery.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UniqueAppEntityQuery](uniqueappentityquery.md)

## See Also

- [protocol UniqueAppEntityQuery](uniqueappentityquery.md)
  A query designed for only returning a single possible value, provided by `uniqueEntity`. Protocol extensions will provide the other required query methods based on that.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uniqueappentityprovider)*