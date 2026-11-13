# combineColumns(_:_:_:into:transform:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Merges three columns that you select by name into a new column.

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
mutating func combineColumns<E1, E2, E3, R>(_ columnName1: String, _ columnName2: String, _ columnName3: String, into newColumnName: String, transform: (E1?, E2?, E3?) throws -> R?) rethrows
```

## Parameters

- `columnName1`: The name of a column.
- `columnName2`: The name of a second column.
- `columnName3`: The name of a third column.
- `newColumnName`: The name of the new column that replaces the three columns.
- `transform`: A closure that combines the corresponding elements of the three columns into one element.

## See Also

### Merging columns
- [func combineColumns<E1, E2, R>(String, String, into: String, transform: (E1?, E2?) throws -> R?) rethrows](./combinecolumns%28_,_,into,transform%29-48ypf.md)
  Merges two columns that you select by name into a new column.
- [func combineColumns<E1, E2, R>(ColumnID<E1>, ColumnID<E2>, into: String, transform: (E1?, E2?) throws -> R?) rethrows](./combinecolumns%28_,_,into,transform%29-85gix.md)
  Merges two columns that you select by column identifier into a new column.
- [func combineColumns<E1, E2, E3, R>(ColumnID<E1>, ColumnID<E2>, ColumnID<E3>, into: String, transform: (E1?, E2?, E3?) throws -> R?) rethrows](./combinecolumns%28_,_,_,into,transform%29-48g26.md)
  Merges three columns that you select by column identifier into a new column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/combinecolumns(_:_:_:into:transform:)-4vyjn)*