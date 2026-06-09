# label

**Framework**: Core Spotlight  
**Kind**: property

A short, LLM-generated description of what the result represents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let label: String?
```

#### Discussion

Use this property to determine what information the model requested. For complex requests, the tool provides the simplest string that describes the current portion of the task. For example, the string might contain a value like “Attachments from John” or “Documents about the deadline.” You can display the string in your app’s interface or use it as an accessibility label.

## See Also

- [let content: SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.property.md)
  The result content — determines what to display and how.
- [let status: SpotlightSearchTool.SearchReply.Status](spotlightsearchtool/searchreply/status-swift.property.md)
  An indicator of whether the current query is complete or still in progress.
- [SpotlightSearchTool.SearchReply.Content](spotlightsearchtool/searchreply/content-swift.enum.md)
  What this set of results represents — determines display strategy.
- [SpotlightSearchTool.SearchReply.Status](spotlightsearchtool/searchreply/status-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchreply/label)*