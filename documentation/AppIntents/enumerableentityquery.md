# EnumerableEntityQuery

**Framework**: App Intents  
**Kind**: protocol

An interface you use to provide a short list of entities that are relatively small in size.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
protocol EnumerableEntityQuery : EntityQuery
```

## Mentions

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)

#### Overview

By implementing an `EnumerableEntityQuery`, you enable the Shortcuts app to generate a Find action and do filtering automatically. Use it in cases where the count of entities is relatively small, and their size in memory is limited. For situations where there may be many thousands of entities, or where individual entities may become large in memory usage, use [`EntityPropertyQuery`](entitypropertyquery.md) to allow better performance by fetching only the entities matching the criteria from your model.

## Topics

### Instance Methods
- [func allEntities() async throws -> Self.Result](enumerableentityquery/allentities.md)
  Returns all available results.
### Type Properties
- [static var findIntentDescription: IntentDescription?](enumerableentityquery/findintentdescription.md)
  Defines how the generated ‘Find’ Shortcuts action of this query type is displayed to the user.

## Relationships

### Inherits From
- [DynamicOptionsProvider](dynamicoptionsprovider.md)
- [EntityQuery](entityquery.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [UniqueAppEntityQuery](uniqueappentityquery.md)
### Conforming Types
- [UniqueAppEntityProvider](uniqueappentityprovider.md)

## See Also

- [protocol EntityQuery](entityquery.md)
  An interface for locating entities using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/enumerableentityquery)*