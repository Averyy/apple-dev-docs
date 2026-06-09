# SpotlightSearchTool.GuidanceLevel.focused(_:)

**Framework**: Core Spotlight  
**Kind**: case

An option to search only specific types of content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case focused(SpotlightSearchTool.ContentDomain = .items)
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Discussion

Choose this option to search attributes only for the specified types of content. You can initialize this value with one or more domains, each of which specifies a particular type of content. During a search, the Spotlight search tool considers only the attributes in the specified domains. The tool also sends data back to the model in a compact format that’s more suitable for models with limited-size context windows.

## See Also

- [SpotlightSearchTool.GuidanceLevel.complete](spotlightsearchtool/guidancelevel/complete.md)
  An option to use all available search techniques.
- [case dynamic(SpotlightSearchTool.GuidanceProfile)](spotlightsearchtool/guidancelevel/dynamic(_:).md)
  An option to search using only the specified techniques.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidancelevel/focused(_:))*