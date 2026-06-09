# guide

**Framework**: Core Spotlight  
**Kind**: property

Options you use to guide the search process that the tool uses to retrieve results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var guide: SpotlightSearchTool.Guide?
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Discussion

The Spotlight search tool employs many techniques to look for results, but some techniques might not be relevant or necessary for your content. Use this property to offer guidance on how to search for your content, and to reduce the amount of data the tool delivers to the model. If you don’t specify custom guidance, the search tool uses all availble techniques, which can take extra time to run and consume additional resources.

## See Also

- [var customStages: [any CustomStage]](spotlightsearchtool/configuration-swift.struct/customstages.md)
  Custom pipeline stages you use to help the Spotlight search tool generate results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/configuration-swift.struct/guide)*