# EntityPropertyQuery.Sort

**Framework**: App Intents  
**Kind**: typealias  
**Role**: Type Alias

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
typealias Sort = EntityQuerySort
```

## See Also

### Searching for entities
- [func entities(matching: [Self.ComparatorMappingType], mode: Self.ComparatorMode, sortedBy: [EntityQuerySort<Self.Entity>], limit: Int?) async throws -> Self.Result](./entities%28matching,mode,sortedby,limit%29.md)
  Retrieves instances matching the supplied comparators.
- [EntityPropertyQuery.ComparatorMode](./comparatormode.md)
- [enum EntityQueryComparatorMode](../entityquerycomparatormode.md)
  Modes that determine how to apply a query’s comparators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitypropertyquery/sort)*