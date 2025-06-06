# sort(on:_:order:)

**Framework**: TabularData  
**Kind**: method

Arranges the rows of a data frame according to two columns that you select by their column identifiers.

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
mutating func sort<T0, T1>(on columnID0: ColumnID<T0>, _ columnID1: ColumnID<T1>, order: Order = .ascending) where T0 : Comparable, T1 : Comparable
```

#### Discussion

> **Note**: Elements with a value of `nil` are less than all non-`nil` values.

Elements with a value of `nil` are less than all non-`nil` values.

## Parameters

- `columnID0`: The identifier of a column.
- `columnID1`: The identifier of another column.
- `order`: A sorting order.

## See Also

- [func sort(on: String, order: Order)](dataframe/sort(on:order:)-4vns7.md)
  Arranges the rows of a data frame according to a column that you select by its name.
- [func sort<T>(on: String, T.Type, order: Order)](dataframe/sort(on:_:order:)-78avw.md)
  Arranges the rows of a data frame according to a column that you select by its name and type.
- [func sort<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows](dataframe/sort(on:_:by:).md)
  Arranges the rows of a data frame according to a column that you select by its name and type, with a predicate.
- [func sort<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows](dataframe/sort(on:by:).md)
  Arranges the rows of a data frame according to a column that you select by its column identifier, with a predicate.
- [func sort<T>(on: ColumnID<T>, order: Order)](dataframe/sort(on:order:)-5ep7w.md)
  Arranges the rows of a data frame according to a column that you select by its column identifier.
- [func sort<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, order: Order)](dataframe/sort(on:_:_:order:).md)
  Arranges the rows of a data frame according to three columns that you select by their column identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/sort(on:_:order:)-8wrkl)*