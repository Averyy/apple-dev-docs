# summary(of:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a categorical summary of the columns you select by name.

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
func summary(of columnNames: String...) -> any GroupSummaries
```

## Return Value

A [`GroupSummaries`](../groupsummaries.md) instance that contains categorical summary of the columns you select.

## Parameters

- `columnNames`: A comma-separated, or variadic, list of column names.

## See Also

### Summarizing a row grouping
- [func summary() -> any GroupSummaries](../rowgrouping/summary%28%29.md)
  Generates a group summaries instance for the columns of the row grouping.
- [func summary(of: [String]) -> any GroupSummaries](../rowgrouping/summary%28of%29.md)
  Generates a group summaries instance for the columns you select by name.
- [protocol GroupSummaries](../groupsummaries.md)
  A collection of group summaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/summary(of:)-n5ia)*