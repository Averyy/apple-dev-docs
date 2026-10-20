# EntityQueryComparatorMode

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

Modes that determine how to apply a query’s comparators.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@frozen
enum EntityQueryComparatorMode
```

## Topics

### Comparator modes
- [EntityQueryComparatorMode.and](./entityquerycomparatormode/and.md)
- [EntityQueryComparatorMode.or](./entityquerycomparatormode/or.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Searching for entities
- [func entities(matching: [Self.ComparatorMappingType], mode: Self.ComparatorMode, sortedBy: [EntityQuerySort<Self.Entity>], limit: Int?) async throws -> Self.Result](./entitypropertyquery/entities%28matching,mode,sortedby,limit%29.md)
  Retrieves instances matching the supplied comparators.
- [EntityPropertyQuery.Sort](./entitypropertyquery/sort.md)
- [EntityPropertyQuery.ComparatorMode](./entitypropertyquery/comparatormode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerycomparatormode)*