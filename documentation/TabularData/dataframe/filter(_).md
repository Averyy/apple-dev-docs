# filter(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns a selection of rows that satisfy a predicate.

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
func filter(_ isIncluded: (DataFrame.Row) throws -> Bool) rethrows -> DataFrame.Slice
```

## Return Value

A data frame slice that contains the rows that satisfy the predicate.

## Parameters

- `isIncluded`: A predicate closure that receives an row and returns a Boolean that indicates whether the slice includes that row.

## See Also

### Creating a slice by filtering rows
- [func filter<T>(on: String, T.Type, (T?) throws -> Bool) rethrows -> DataFrame.Slice](./filter%28on,_,_%29.md)
  Returns a selection of rows that satisfy a predicate in the columns you select by name.
- [func filter<T>(on: ColumnID<T>, (T?) throws -> Bool) rethrows -> DataFrame.Slice](./filter%28on,_%29.md)
  Returns a selection of rows that satisfy a predicate in the columns you select by column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/filter(_:))*