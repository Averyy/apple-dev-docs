# SearchTextResult

**Framework**: Core Spotlight  
**Kind**: struct

LLM-generated text summary or analysis from a pipeline stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchTextResult
```

## Topics

### Creating a text result
- [init(body: String, header: String?)](searchtextresult/init(body:header:).md)
### Getting the result details
- [let header: String?](searchtextresult/header.md)
  A short description of what this text represents.
- [let body: String](searchtextresult/body.md)
  The text body.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct SearchCount](searchcount.md)
  A scalar count result (e.g., “47 emails from John”).
- [struct SearchResultsTable](searchresultstable.md)
  Tabulated result data — rows with typed columns for display or spreadsheet export.
- [struct SearchStatistic](searchstatistic.md)
  A scalar statistic derived from search results (sum, average, max, min, median, stddev).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchtextresult)*