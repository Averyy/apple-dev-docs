# SpotlightSearchTool.SearchReply.Content

**Framework**: Core Spotlight  
**Kind**: enum

What this set of results represents — determines display strategy.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Content
```

## Topics

### Enumeration Cases
- [SpotlightSearchTool.SearchReply.Content.count(_:)](spotlightsearchtool/searchreply/content-swift.enum/count(_:).md)
  A scalar count answer (e.g., “How many emails from John?” → 47).
- [case groupedItems([SearchableItemAttribute : [CSSearchableItem]])](spotlightsearchtool/searchreply/content-swift.enum/groupeditems(_:).md)
  Items partitioned by an attribute value (e.g. content type).
- [SpotlightSearchTool.SearchReply.Content.items(_:)](spotlightsearchtool/searchreply/content-swift.enum/items(_:).md)
  Ssearch result items (emails, files, etc.) — display as a list.
- [SpotlightSearchTool.SearchReply.Content.scoredItems(_:)](spotlightsearchtool/searchreply/content-swift.enum/scoreditems(_:).md)
  Items annotated with caller-assigned relevance scores.
- [SpotlightSearchTool.SearchReply.Content.statistic(_:)](spotlightsearchtool/searchreply/content-swift.enum/statistic(_:).md)
  A scalar statistic (sum, average, max, min, median, stddev).
- [SpotlightSearchTool.SearchReply.Content.table(_:)](spotlightsearchtool/searchreply/content-swift.enum/table(_:).md)
  Tabulated data — rows of labeled values, suitable for a table or chart.
- [SpotlightSearchTool.SearchReply.Content.text(_:)](spotlightsearchtool/searchreply/content-swift.enum/text(_:).md)
  LLM-generated text summary or analysis.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let content: SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.property.md)
  The result content — determines what to display and how.
- [let label: String?](spotlightsearchtool/searchreply/label.md)
  A short, LLM-generated description of what the result represents.
- [let status: SpotlightSearchTool.SearchReply.Status](spotlightsearchtool/searchreply/status-swift.property.md)
  An indicator of whether the current query is complete or still in progress.
- [SpotlightSearchTool.SearchReply.Status](spotlightsearchtool/searchreply/status-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/content-swift.enum)*