# explodingColumn(_:_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame by replacing each row in a collection column that you select by name, with a new row for each element in the original row’s collection.

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
func explodingColumn<T>(_ name: String, _ type: T.Type) -> DataFrame where T : Collection
```

## Parameters

- `name`: A column name.
- `type`: The underlying type of the column.

## See Also

### Expanding a column
- [func explodeColumn<T>(String, T.Type)](./explodecolumn%28_,_%29.md)
  Replaces each row in a collection column that you select by name, with a new row for each element in the original row’s collection.
- [func explodeColumn<T>(ColumnID<T>)](./explodecolumn%28_%29.md)
  Replaces each row in a collection column that you select by column identifier, with a new row for each element in the original row’s collection.
- [func explodingColumn<T>(ColumnID<T>) -> DataFrame](./explodingcolumn%28_%29.md)
  Generates a data frame by replacing each row in a collection column that you select by column identifier, with a new row for each element in the original row’s collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/explodingcolumn(_:_:))*