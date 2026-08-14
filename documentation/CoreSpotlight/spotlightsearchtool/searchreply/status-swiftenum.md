# SpotlightSearchTool.SearchReply.Status

**Framework**: Core Spotlight  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Status
```

## Topics

### Enumeration Cases
- [SpotlightSearchTool.SearchReply.Status.complete](spotlightsearchtool/searchreply/status-swift.enum/complete.md)
  This is the final set of results for this `queryToken`.
- [SpotlightSearchTool.SearchReply.Status.partial](spotlightsearchtool/searchreply/status-swift.enum/partial.md)
  More results may be yielded for this `queryToken`.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let content: SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.property.md)
  The result content — determines what to display and how.
- [let label: String?](spotlightsearchtool/searchreply/label.md)
  A short, LLM-generated description of what the result represents.
- [let status: SpotlightSearchTool.SearchReply.Status](spotlightsearchtool/searchreply/status-swift.property.md)
  An indicator of whether the current query is complete or still in progress.
- [SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.enum.md)
  What this set of results represents — determines display strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/status-swift.enum)*