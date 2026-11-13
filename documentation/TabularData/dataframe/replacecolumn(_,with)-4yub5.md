# replaceColumn(_:with:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Replaces a column in the data frame, by name, with a typed column.

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
mutating func replaceColumn<T>(_ name: String, with newColumn: Column<T>)
```

## Parameters

- `name`: The name of a column in the data frame.
- `newColumn`: Another column that replaces the column.

## See Also

### Replacing a column
- [func replaceColumn(String, with: AnyColumn)](./replacecolumn%28_,with%29-2b3u3.md)
  Replaces a column in the data frame, by name, with a type-erased column.
- [func replaceColumn<T>(ColumnID<T>, with: AnyColumn)](./replacecolumn%28_,with%29-9sn9i.md)
  Replaces a column in the data frame, by column identifier, with a type-erased column.
- [func replaceColumn<T, U>(ColumnID<T>, with: Column<U>)](./replacecolumn%28_,with%29-oa9g.md)
  Replaces a column in the data frame, by column identifier, with a typed column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/replacecolumn(_:with:)-4yub5)*