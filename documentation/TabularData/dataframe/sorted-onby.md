# sorted(on:by:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier, with a predicate.

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
func sorted<T>(on columnID: ColumnID<T>, by areInIncreasingOrder: (T, T) throws -> Bool) rethrows -> DataFrame
```

#### Discussion

> **Note**: Elements with a value of `nil` are less than all non-`nil` values.

Elements with a value of `nil` are less than all non-`nil` values.

## Parameters

- `columnID`: The identifier of a column.
- `areInIncreasingOrder`: A closure that returns a Boolean that indicates   whether the two elements are in increasing order.

## See Also

- [func sorted<T>(on: String, T.Type, order: Order) -> DataFrame](dataframe/sorted(on:_:order:)-7gt7j.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type.
- [func sorted<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframe/sorted(on:_:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type, with a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/sorted(on:by:))*