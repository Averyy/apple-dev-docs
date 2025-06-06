# summary(ofColumns:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame that summarizes the columns you select by index.

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
func summary(ofColumns columnIndices: Int...) -> DataFrame
```

## Parameters

- `columnIndices`: A comma-separated, or variadic, list of column indices in the data frame slice.

## See Also

- [func summary() -> DataFrame](dataframe/slice/summary.md)
  Generates a data frame that summarizes the columns of the data frame slice.
- [func summary(of: String...) -> DataFrame](dataframe/slice/summary(of:).md)
  Generates a data frame that summarizes the columns you select by name.
- [enum SummaryColumnIDs](summarycolumnids.md)
  The summary data frame column identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/summary(ofcolumns:))*