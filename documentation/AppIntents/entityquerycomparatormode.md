# EntityQueryComparatorMode

**Framework**: App Intents  
**Kind**: enum

Modes that determine how to apply a query’s comparators.

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
@frozen
enum EntityQueryComparatorMode
```

## Topics

### Comparator modes
- [EntityQueryComparatorMode.and](entityquerycomparatormode/and.md)
- [EntityQueryComparatorMode.or](entityquerycomparatormode/or.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func entities(matching: [Self.ComparatorMappingType], mode: Self.ComparatorMode, sortedBy: [EntityQuerySort<Self.Entity>], limit: Int?) async throws -> Self.Result](entitypropertyquery/entities(matching:mode:sortedby:limit:).md)
  Retrieves instances matching the supplied comparators.
- [EntityPropertyQuery.Sort](entitypropertyquery/sort.md)
- [EntityPropertyQuery.ComparatorMode](entitypropertyquery/comparatormode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerycomparatormode)*