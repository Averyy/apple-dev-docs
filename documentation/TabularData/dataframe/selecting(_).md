# selecting(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame that includes only the column selection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func selecting(_ selection: ColumnSelection) -> DataFrame
```

## Return Value

A new data frame including only the selected columns.

## Parameters

- `selection`: A selection of columns.

## See Also

### Selecting columns
- [subscript<S>(S) -> DataFrame](./subscript%28_%29-4war.md)
  Generates a data frame that includes the columns in a sequence of column names.
- [func selecting(columnNames: String...) -> DataFrame](./selecting%28columnnames%29-pp1o.md)
  Generates a data frame that includes the columns you select with a list of names.
- [func selecting<S>(columnNames: S) -> DataFrame](./selecting%28columnnames%29-3kms8.md)
  Generates a data frame that includes the columns you select with a sequence of names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/selecting(_:))*