# summary(ofColumns:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

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

- `columnIndices`: A comma-separated, or variadic, list of column indices in the data frame.

## See Also

### Summarizing a Data Frame
- [func summary() -> DataFrame](./summary%28%29.md)
  Generates a data frame that summarizes the columns of the data frame.
- [func summary(of: String...) -> DataFrame](./summary%28of%29.md)
  Generates a data frame that summarizes the columns you select by name.
- [enum SummaryColumnIDs](../summarycolumnids.md)
  The summary data frame column identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/summary(ofcolumns:))*