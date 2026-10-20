# summary()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a group summaries instance for the columns of the row grouping.

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
func summary() -> any GroupSummaries
```

Available when `GroupingKey` conforms to `Hashable`.

## See Also

### Summarizing a Row Grouping
- [func summary(of: [String]) -> any GroupSummaries](./summary%28of%29.md)
  Generates a group summaries instance for the columns you select by name.
- [protocol GroupSummaries](../groupsummaries.md)
  A collection of group summaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/summary())*