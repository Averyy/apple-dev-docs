# filter(on:_:_:)

**Framework**: TabularData  
**Kind**: method

Returns a selection of rows that satisfy a predicate in the columns you select by name.

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
func filter<T>(on columnName: String, _ type: T.Type, _ isIncluded: (T?) throws -> Bool) rethrows -> DataFrame.Slice
```

#### Return Value

A data frame slice that contains the rows that satisfy the predicate.

## Parameters

- `columnName`: The name of a column.
- `type`: The type of the column.
- `isIncluded`: A predicate closure that receives an element of the column as its argument,   and returns a Boolean that indicates whether the slice includes the element’s row.

## See Also

- [func filter<T>(on: ColumnID<T>, (T?) throws -> Bool) rethrows -> DataFrame.Slice](dataframe/slice/filter(on:_:).md)
  Returns a selection of rows that satisfy a predicate in the columns you select by column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/filter(on:_:_:))*