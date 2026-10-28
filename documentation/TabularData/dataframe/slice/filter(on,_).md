# filter(on:_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns a selection of rows that satisfy a predicate in the columns you select by column identifier.

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
func filter<T>(on columnID: ColumnID<T>, _ isIncluded: (T?) throws -> Bool) rethrows -> DataFrame.Slice
```

## Return Value

A data frame slice that contains the rows that satisfy the predicate.

## Parameters

- `columnID`: The identifier of a column in the slice.
- `isIncluded`: A predicate closure that receives an element of the column as its argument, and returns a Boolean that indicates whether the slice includes the element’s row.

## See Also

### Creating a Slice by Filtering Rows
- [func filter<T>(on: String, T.Type, (T?) throws -> Bool) rethrows -> DataFrame.Slice](./filter%28on,_,_%29.md)
  Returns a selection of rows that satisfy a predicate in the columns you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/filter(on:_:))*