# UniqueAppEntityQuery

**Framework**: App Intents  
**Kind**: protocol

A query designed for only returning a single possible value, provided by `uniqueEntity`. Protocol extensions will provide the other required query methods based on that.

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
protocol UniqueAppEntityQuery : EnumerableEntityQuery where Self.Entity : UniqueAppEntity
```

## Topics

### Associated Types
- [associatedtype Unique](uniqueappentityquery/unique.md)
### Instance Methods
- [func uniqueEntity() async throws -> Self.Unique](uniqueappentityquery/uniqueentity.md)

## Relationships

### Inherits From
- [DynamicOptionsProvider](dynamicoptionsprovider.md)
- [EntityQuery](entityquery.md)
- [EnumerableEntityQuery](enumerableentityquery.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [UniqueAppEntityProvider](uniqueappentityprovider.md)

## See Also

- [struct UniqueAppEntityProvider](uniqueappentityprovider.md)
  A simplified query type conforming to `UniqueAppEntityQuery`.  Use this as the value of the `defaultQuery` of an entity conforming to `UniqueAppEntity`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uniqueappentityquery)*