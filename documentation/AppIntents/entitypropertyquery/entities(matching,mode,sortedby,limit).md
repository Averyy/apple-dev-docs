# entities(matching:mode:sortedBy:limit:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Retrieves instances matching the supplied comparators.

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
func entities(matching comparators: [Self.ComparatorMappingType], mode: Self.ComparatorMode, sortedBy: [EntityQuerySort<Self.Entity>], limit: Int?) async throws -> Self.Result
```

## Parameters

- `comparators`: Array containing mapped values for comparators that entities need to match
- `mode`: Whether entity instances should match any or all comparators
- `sortedBy`: Array describing the query’s sorting order
- `limit`: Optional limit on the number of entity instances to return

## See Also

### Searching for entities
- [EntityPropertyQuery.Sort](./sort.md)
- [EntityPropertyQuery.ComparatorMode](./comparatormode.md)
- [enum EntityQueryComparatorMode](../entityquerycomparatormode.md)
  Modes that determine how to apply a query’s comparators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitypropertyquery/entities(matching:mode:sortedby:limit:))*