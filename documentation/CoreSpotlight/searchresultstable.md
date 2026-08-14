# SearchResultsTable

**Framework**: Core Spotlight  
**Kind**: struct

Tabulated result data — rows with typed columns for display or spreadsheet export.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchResultsTable
```

## Topics

### Creating the search count
- [init(header: String?, columns: [SearchResultsTable.Column], rows: [SearchResultsTable.Row])](searchresultstable/init(header:columns:rows:).md)
### Getting the column and row details
- [let header: String?](searchresultstable/header.md)
  What this table represents (e.g., “Emails per month from John”).
- [let columns: [SearchResultsTable.Column]](searchresultstable/columns.md)
  Column definitions with name and type hint.
- [let rows: [SearchResultsTable.Row]](searchresultstable/rows.md)
  Data rows — each row’s values array matches `columns` by index.
- [SearchResultsTable.Column](searchresultstable/column.md)
- [SearchResultsTable.Row](searchresultstable/row.md)
### Getting cell details
- [SearchResultsTable.Value](searchresultstable/value.md)
  A cell value — typed so the host app can format, sort, or export correctly.
- [SearchResultsTable.ValueType](searchresultstable/valuetype.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct SearchCount](searchcount.md)
  A scalar count result (e.g., “47 emails from John”).
- [struct SearchStatistic](searchstatistic.md)
  A scalar statistic derived from search results (sum, average, max, min, median, stddev).
- [struct SearchTextResult](searchtextresult.md)
  LLM-generated text summary or analysis from a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchresultstable)*