# SpotlightSearchTool.SearchReply.QueryToken

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

An opaque type you use to identify a single call to the Spotlight search tool.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct QueryToken
```

## Overview

When processing a request, a model might call the Spotlight search tool multiple times to retrieve results. Each time the model calls the Spotlight search tool’s [`call(arguments:)`](../../../FoundationModels/tool/call%28arguments%29.md) method, the tool generates a new `QueryToken` to track that request. When delivering results to your app, the tool includes this token in the [`SpotlightSearchTool.SearchReply`](../searchreply.md) structures it delivers. Use the token to associate that data with a specific query.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the tokens
- [let queryToken: SpotlightSearchTool.SearchReply.QueryToken](./querytoken-swift.property.md)
  An opaque value you use to identify the query that generated the reply.
- [let stageToken: SpotlightSearchTool.SearchReply.StageToken](./stagetoken-swift.property.md)
  An opaque value you use to identify the pipeline stage that generated the reply.
- [SpotlightSearchTool.SearchReply.StageToken](./stagetoken-swift.struct.md)
  An opaque type you use to identify a single pipeline stage within the Spotlight search tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/querytoken-swift.struct)*