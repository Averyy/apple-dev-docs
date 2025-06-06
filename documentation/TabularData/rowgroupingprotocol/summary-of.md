# summary(of:)

**Framework**: TabularData  
**Kind**: method  
**Required**: Yes

Generates a group summaries instance of the row grouping’s columns you select by name.

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
func summary(of columnNames: [String]) -> any GroupSummaries
```

## Parameters

- `columnNames`: An array of column names.

## See Also

- [func summary() -> any GroupSummaries](rowgroupingprotocol/summary.md)
  Generates a group summaries instance of the row grouping’s columns.
- [protocol GroupSummaries](groupsummaries.md)
  A collection of group summaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/summary(of:))*