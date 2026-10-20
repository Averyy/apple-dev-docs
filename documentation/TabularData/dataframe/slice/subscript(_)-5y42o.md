# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Generates a data frame slice that includes the columns in a sequence of column names.

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
subscript<S>(columnNames: S) -> DataFrame.Slice where S : Sequence, S.Element == String { get }
```

#### Return Value

A new data frame slice.

## Parameters

- `columnNames`: A sequence of column names.

## See Also

- [func selecting<S>(columnNames: S) -> DataFrame.Slice](dataframe/slice/selecting(columnnames:)-9l8oe.md)
  Generates a data frame slice that includes the columns you select with a sequence of names.
- [func selecting(columnNames: String...) -> DataFrame.Slice](dataframe/slice/selecting(columnnames:)-48kji.md)
  Generates a data frame slice that includes the columns you select with a list of names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/subscript(_:)-5y42o)*