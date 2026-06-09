# status

**Framework**: Core Spotlight  
**Kind**: property

An indicator of whether the current query is complete or still in progress.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let status: SpotlightSearchTool.SearchReply.Status
```

#### Discussion

The of this property is [`SpotlightSearchTool.SearchReply.Status.partial`](spotlightsearchtool/searchreply/status-swift.enum/partial.md) when the system has more replies to deliver for the same [`queryToken`](spotlightsearchtool/searchreply/querytoken-swift.property.md) value. When delivering the last reply for a query, the tool sets this value to [`SpotlightSearchTool.SearchReply.Status.complete`](spotlightsearchtool/searchreply/status-swift.enum/complete.md). Use this value to track changes to the current query. For example, you might choose to partition data for each query and display them separately in your interface.

## See Also

- [let content: SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.property.md)
  The result content — determines what to display and how.
- [let label: String?](spotlightsearchtool/searchreply/label.md)
  A short, LLM-generated description of what the result represents.
- [SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.enum.md)
  What this set of results represents — determines display strategy.
- [SpotlightSearchTool.SearchReply.Status](spotlightsearchtool/searchreply/status-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/status-swift.property)*