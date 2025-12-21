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
- [init(() async throws -> Entity)](uniqueappentityprovider/init(_:).md)

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