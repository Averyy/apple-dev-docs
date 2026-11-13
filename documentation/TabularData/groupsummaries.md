# GroupSummaries

**Framework**: TabularData  
**Kind**: protocol  
**Role**: Protocol

A collection of group summaries.

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
protocol GroupSummaries : CustomStringConvertible
```

## Topics

### Accessing summaries
- [subscript(Any?...) -> DataFrame?](./groupsummaries/subscript%28_%29.md)
  Retrieves one or more summaries by their group keys.
### Describing group summaries
- [var description: String](./groupsummaries/description.md)
  A text representation of the group summaries.
- [func description(options: FormattingOptions) -> String](./groupsummaries/description%28options%29.md)
  Generates a text representation of the group summaries.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/customstringconvertible.md)

## See Also

### Summarizing a row grouping
- [func summary() -> any GroupSummaries](./rowgrouping/summary%28%29.md)
  Generates a group summaries instance for the columns of the row grouping.
- [func summary(of: [String]) -> any GroupSummaries](./rowgrouping/summary%28of%29.md)
  Generates a group summaries instance for the columns you select by name.
- [func summary(of: String...) -> any GroupSummaries](./rowgroupingprotocol/summary%28of%29-n5ia.md)
  Generates a categorical summary of the columns you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/groupsummaries)*