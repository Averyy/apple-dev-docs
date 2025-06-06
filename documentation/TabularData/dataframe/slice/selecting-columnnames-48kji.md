# selecting(columnNames:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame slice that includes the columns you select with a list of names.

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
func selecting(columnNames: String...) -> DataFrame.Slice
```

#### Return Value

A new data frame slice.

## Parameters

- `columnNames`: A comma-separated, or variadic, list of column names.

## See Also

- [subscript<S>(S) -> DataFrame.Slice](dataframe/slice/subscript(_:)-5y42o.md)
  Generates a data frame slice that includes the columns in a sequence of column names.
- [func selecting<S>(columnNames: S) -> DataFrame.Slice](dataframe/slice/selecting(columnnames:)-9l8oe.md)
  Generates a data frame slice that includes the columns you select with a sequence of names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/selecting(columnnames:)-48kji)*