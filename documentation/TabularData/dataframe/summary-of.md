# summary(of:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame that summarizes the columns you select by name.

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
func summary(of columnNames: String...) -> DataFrame
```

## Parameters

- `columnNames`: A comma-separated, or variadic, list of column names in the data frame.

## See Also

- [func summary() -> DataFrame](dataframe/summary.md)
  Generates a data frame that summarizes the columns of the data frame.
- [func summary(ofColumns: Int...) -> DataFrame](dataframe/summary(ofcolumns:).md)
  Generates a data frame that summarizes the columns you select by index.
- [enum SummaryColumnIDs](summarycolumnids.md)
  The summary data frame column identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/summary(of:))*