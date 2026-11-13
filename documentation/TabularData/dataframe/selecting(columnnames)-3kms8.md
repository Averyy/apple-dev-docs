# selecting(columnNames:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame that includes the columns you select with a sequence of names.

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
func selecting<S>(columnNames: S) -> DataFrame where S : Sequence, S.Element == String
```

## Return Value

A new data frame.

## Parameters

- `columnNames`: A sequence of column names.

## See Also

### Selecting columns
- [subscript<S>(S) -> DataFrame](./subscript%28_%29-4war.md)
  Generates a data frame that includes the columns in a sequence of column names.
- [func selecting(columnNames: String...) -> DataFrame](./selecting%28columnnames%29-pp1o.md)
  Generates a data frame that includes the columns you select with a list of names.
- [func selecting(ColumnSelection) -> DataFrame](./selecting%28_%29.md)
  Generates a data frame that includes only the column selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/selecting(columnnames:)-3kms8)*