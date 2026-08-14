# SpotlightSearchTool.SearchReply.QueryToken

**Framework**: Core Spotlight  
**Kind**: struct

An opaque type you use to identify a single call to the Spotlight search tool.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct QueryToken
```

#### Overview

When processing a request, a model might call the Spotlight search tool multiple times to retrieve results. Each time the model calls the Spotlight search tool’s [`call(arguments:)`](https://developer.apple.com/documentation/foundationmodels/tool/call(arguments:)) method, the tool generates a new `QueryToken` to track that request. When delivering results to your app, the tool includes this token in the [`SpotlightSearchTool.SearchReply`](spotlightsearchtool/searchreply.md) structures it delivers. Use the token to associate that data with a specific query.

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
- [SpotlightSearchTool.SearchReply.StageToken](spotlightsearchtool/searchreply/stagetoken-swift.struct.md)
  An opaque type you use to identify a single pipeline stage within the Spotlight search tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/querytoken-swift.struct)*