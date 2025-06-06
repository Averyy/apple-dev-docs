# sorted(on:_:by:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type, with a predicate.

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
func sorted<T>(on columnName: String, _ type: T.Type, by areInIncreasingOrder: (T, T) throws -> Bool) rethrows -> DataFrame
```

#### Discussion

> **Note**: Elements with a value of `nil` are less than all non-`nil` values.

Elements with a value of `nil` are less than all non-`nil` values.

## Parameters

- `columnName`: The name of a column.
- `type`: The column’s type.
- `areInIncreasingOrder`: A closure that returns a Boolean that indicates   whether the two elements are in increasing order.

## See Also

- [func sorted(on: String, order: Order) -> DataFrame](dataframe/slice/sorted(on:order:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name.
- [func sorted<T>(on: String, T.Type, order: Order) -> DataFrame](dataframe/slice/sorted(on:_:order:)-37i2f.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type.
- [func sorted<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframe/slice/sorted(on:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier, with a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/sorted(on:_:by:))*