# SpotlightSearchTool.SearchReply.Content

**Framework**: Core Spotlight  
**Kind**: enum  
**Role**: Enumeration

What this set of results represents — determines display strategy.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Content
```

## Topics

### Enumeration Cases
- [SpotlightSearchTool.SearchReply.Content.count(_:)](./content-swift.enum/count%28_%29.md)
  A scalar count answer (e.g., “How many emails from John?” → 47).
- [case groupedItems([SearchableItemAttribute : [SearchableItem]])](./content-swift.enum/groupeditems%28_%29.md)
  Items partitioned by an attribute value (e.g. content type).
- [SpotlightSearchTool.SearchReply.Content.items(_:)](./content-swift.enum/items%28_%29.md)
  Ssearch result items (emails, files, etc.) — display as a list.
- [SpotlightSearchTool.SearchReply.Content.scoredItems(_:)](./content-swift.enum/scoreditems%28_%29.md)
  Items annotated with caller-assigned relevance scores.
- [SpotlightSearchTool.SearchReply.Content.statistic(_:)](./content-swift.enum/statistic%28_%29.md)
  A scalar statistic (sum, average, max, min, median, stddev).
- [SpotlightSearchTool.SearchReply.Content.table(_:)](./content-swift.enum/table%28_%29.md)
  Tabulated data — rows of labeled values, suitable for a table or chart.
- [SpotlightSearchTool.SearchReply.Content.text(_:)](./content-swift.enum/text%28_%29.md)
  LLM-generated text summary or analysis.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the reply details
- [let content: SpotlightSearchTool.SearchReply.Content](./content-swift.property.md)
  The result content — determines what to display and how.
- [let label: String?](./label.md)
  A short, LLM-generated description of what the result represents.
- [let status: SpotlightSearchTool.SearchReply.Status](./status-swift.property.md)
  An indicator of whether the current query is complete or still in progress.
- [SpotlightSearchTool.SearchReply.Status](./status-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/content-swift.enum)*