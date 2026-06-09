# stageToken

**Framework**: Core Spotlight  
**Kind**: property

An opaque value you use to identify the pipeline stage that generated the reply.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let stageToken: SpotlightSearchTool.SearchReply.StageToken
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Discussion

The Spotlight search tool provides several ways to search content, and implements each technique as an independent stage. For a given query, a model can run multiple stages to generate the results of the query. Use this property to associate search reply structures with a specific stage. The token itself is an opaque value you save and compare against tokens in other search replies. You might use this value to partition the data you receive.

## See Also

- [let queryToken: SpotlightSearchTool.SearchReply.QueryToken](spotlightsearchtool/searchreply/querytoken-swift.property.md)
  An opaque value you use to identify the query that generated the reply.
- [SpotlightSearchTool.SearchReply.QueryToken](spotlightsearchtool/searchreply/querytoken-swift.struct.md)
  An opaque type you use to identify a single call to the Spotlight search tool.
- [SpotlightSearchTool.SearchReply.StageToken](spotlightsearchtool/searchreply/stagetoken-swift.struct.md)
  An opaque type you use to identify a single pipeline stage within the Spotlight search tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/stagetoken-swift.property)*