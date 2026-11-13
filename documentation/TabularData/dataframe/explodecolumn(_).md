# explodeColumn(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Replaces each row in a collection column that you select by column identifier, with a new row for each element in the original row’s collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func explodeColumn<T>(_ id: ColumnID<T>) where T : Collection
```

## Parameters

- `id`: A column identifier.

## See Also

### Expanding a column
- [func explodeColumn<T>(String, T.Type)](./explodecolumn%28_,_%29.md)
  Replaces each row in a collection column that you select by name, with a new row for each element in the original row’s collection.
- [func explodingColumn<T>(String, T.Type) -> DataFrame](./explodingcolumn%28_,_%29.md)
  Generates a data frame by replacing each row in a collection column that you select by name, with a new row for each element in the original row’s collection.
- [func explodingColumn<T>(ColumnID<T>) -> DataFrame](./explodingcolumn%28_%29.md)
  Generates a data frame by replacing each row in a collection column that you select by column identifier, with a new row for each element in the original row’s collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/explodecolumn(_:))*