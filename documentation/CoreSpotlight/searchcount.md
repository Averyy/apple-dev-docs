# SearchCount

**Framework**: Core Spotlight  
**Kind**: struct

A scalar count result (e.g., “47 emails from John”).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchCount
```

## Topics

### Creating the search count
- [init(value: Int, header: String?)](searchcount/init(value:header:).md)
### Getting the counted information
- [let header: String?](searchcount/header.md)
  A short description of what was counted (e.g., “Emails from John since 2003”).
- [let value: Int](searchcount/value.md)
  The count value.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SearchResultsTable](searchresultstable.md)
  Tabulated result data — rows with typed columns for display or spreadsheet export.
- [struct SearchStatistic](searchstatistic.md)
  A scalar statistic derived from search results (sum, average, max, min, median, stddev).
- [struct SearchTextResult](searchtextresult.md)
  LLM-generated text summary or analysis from a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchcount)*