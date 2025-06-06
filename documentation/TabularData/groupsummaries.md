# GroupSummaries

**Framework**: TabularData  
**Kind**: protocol

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

### Instance Properties
- [var description: String](groupsummaries/description.md)
  A text representation of the group summaries.
### Instance Methods
- [func description(options: FormattingOptions) -> String](groupsummaries/description(options:).md)
  Generates a text representation of the group summaries.
### Subscripts
- [subscript(Any?...) -> DataFrame?](groupsummaries/subscript(_:).md)
  Retrieves one or more summaries by their group keys.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [func summary() -> any GroupSummaries](rowgrouping/summary.md)
  Generates a group summaries instance for the columns of the row grouping.
- [func summary(of: [String]) -> any GroupSummaries](rowgrouping/summary(of:).md)
  Generates a group summaries instance for the columns you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/groupsummaries)*