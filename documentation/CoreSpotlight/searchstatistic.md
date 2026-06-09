# SearchStatistic

**Framework**: Core Spotlight  
**Kind**: struct

A scalar statistic derived from search results (sum, average, max, min, median, stddev).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchStatistic
```

## Topics

### Creating a search statistic
- [init(name: String, value: Double, header: String?)](searchstatistic/init(name:value:header:).md)
### Getting the statistic details
- [let name: String](searchstatistic/name.md)
  The statistic name (e.g., “average”, “max”, “total”).
- [let header: String?](searchstatistic/header.md)
  A short description of what was computed (e.g., “Average file size”).
- [let value: Double](searchstatistic/value.md)
  The computed value.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SearchCount](searchcount.md)
  A scalar count result (e.g., “47 emails from John”).
- [struct SearchResultsTable](searchresultstable.md)
  Tabulated result data — rows with typed columns for display or spreadsheet export.
- [struct SearchTextResult](searchtextresult.md)
  LLM-generated text summary or analysis from a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchstatistic)*