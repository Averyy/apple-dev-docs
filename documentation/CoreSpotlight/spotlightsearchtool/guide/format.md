# format

**Framework**: Core Spotlight  
**Kind**: property

The representation format for tool responses returned to the model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let format: SpotlightSearchTool.FormatLevel
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Discussion

Controls how search results are serialized in the model’s context window. Use [`SpotlightSearchTool.FormatLevel.compact`](spotlightsearchtool/formatlevel/compact.md) to reduce token consumption when working with small-context models or long conversations.

## See Also

- [let level: SpotlightSearchTool.GuidanceLevel](spotlightsearchtool/guide/level.md)
  The guidance for the model to use during a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guide/format)*