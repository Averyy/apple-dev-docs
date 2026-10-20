# SpotlightSearchTool.SearchReply.Status

**Framework**: Core Spotlight  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Status
```

## Topics

### Enumeration Cases
- [SpotlightSearchTool.SearchReply.Status.complete](./status-swift.enum/complete.md)
  This is the final set of results for this `queryToken`.
- [SpotlightSearchTool.SearchReply.Status.partial](./status-swift.enum/partial.md)
  More results may be yielded for this `queryToken`.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
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
- [SpotlightSearchTool.SearchReply.Content](./content-swift.enum.md)
  What this set of results represents — determines display strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/status-swift.enum)*