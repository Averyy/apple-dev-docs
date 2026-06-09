# SpotlightSearchTool.SearchReply

**Framework**: Core Spotlight  
**Kind**: struct

A set of search results with routing metadata for host app consumption.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchReply
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

## Topics

### Getting the reply details
- [let content: SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.property.md)
  The result content — determines what to display and how.
- [let label: String?](spotlightsearchtool/searchreply/label.md)
  A short, LLM-generated description of what the result represents.
- [let status: SpotlightSearchTool.SearchReply.Status](spotlightsearchtool/searchreply/status-swift.property.md)
  An indicator of whether the current query is complete or still in progress.
- [SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.enum.md)
  What this set of results represents — determines display strategy.
- [SpotlightSearchTool.SearchReply.Status](spotlightsearchtool/searchreply/status-swift.enum.md)
### Getting the tokens
- [let queryToken: SpotlightSearchTool.SearchReply.QueryToken](spotlightsearchtool/searchreply/querytoken-swift.property.md)
  An opaque value you use to identify the query that generated the reply.
- [let stageToken: SpotlightSearchTool.SearchReply.StageToken](spotlightsearchtool/searchreply/stagetoken-swift.property.md)
  An opaque value you use to identify the pipeline stage that generated the reply.
- [SpotlightSearchTool.SearchReply.QueryToken](spotlightsearchtool/searchreply/querytoken-swift.struct.md)
  An opaque type you use to identify a single call to the Spotlight search tool.
- [SpotlightSearchTool.SearchReply.StageToken](spotlightsearchtool/searchreply/stagetoken-swift.struct.md)
  An opaque type you use to identify a single pipeline stage within the Spotlight search tool.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var searchResults: some AsyncSequence<SpotlightSearchTool.SearchReply, Never>](spotlightsearchtool/searchresults.md)
  An asynchronous stream that delivers the results of a search to your app for processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply)*