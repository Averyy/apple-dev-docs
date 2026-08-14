# SpotlightSearchTool.SearchReply.StageToken

**Framework**: Core Spotlight  
**Kind**: struct

An opaque type you use to identify a single pipeline stage within the Spotlight search tool.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct StageToken
```

#### Overview

Within a single call to the Spotlight search tool’s [`call(arguments:)`](https://developer.apple.com/documentation/foundationmodels/tool/call(arguments:)) method, the tool can run one or more pipeline stages to deliver the requested results. Each stage corresponds to a specific task needed to generate the results. For example, one stage might rank the search results based on their relevance. When delivering results to your app, the tool includes a `StageToken` value in the [`SpotlightSearchTool.SearchReply`](spotlightsearchtool/searchreply.md) structure it delivers. You can use the token to associate that data with a particular processing stage of the tool.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let queryToken: SpotlightSearchTool.SearchReply.QueryToken](spotlightsearchtool/searchreply/querytoken-swift.property.md)
  An opaque value you use to identify the query that generated the reply.
- [let stageToken: SpotlightSearchTool.SearchReply.StageToken](spotlightsearchtool/searchreply/stagetoken-swift.property.md)
  An opaque value you use to identify the pipeline stage that generated the reply.
- [SpotlightSearchTool.SearchReply.QueryToken](spotlightsearchtool/searchreply/querytoken-swift.struct.md)
  An opaque type you use to identify a single call to the Spotlight search tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/stagetoken-swift.struct)*