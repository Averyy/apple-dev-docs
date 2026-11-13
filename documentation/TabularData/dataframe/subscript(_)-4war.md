# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Generates a data frame that includes the columns in a sequence of column names.

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
subscript<S>(columnNames: S) -> DataFrame where S : Sequence, S.Element == String { get }
```

## Return Value

A new data frame.

## Parameters

- `columnNames`: A sequence of column names.

## See Also

### Selecting columns
- [func selecting(columnNames: String...) -> DataFrame](./selecting%28columnnames%29-pp1o.md)
  Generates a data frame that includes the columns you select with a list of names.
- [func selecting<S>(columnNames: S) -> DataFrame](./selecting%28columnnames%29-3kms8.md)
  Generates a data frame that includes the columns you select with a sequence of names.
- [func selecting(ColumnSelection) -> DataFrame](./selecting%28_%29.md)
  Generates a data frame that includes only the column selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/subscript(_:)-4war)*