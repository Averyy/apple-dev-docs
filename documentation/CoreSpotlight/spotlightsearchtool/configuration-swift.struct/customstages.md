# customStages

**Framework**: Core Spotlight  
**Kind**: property

Custom pipeline stages you use to help the Spotlight search tool generate results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var customStages: [any CustomStage] { get set }
```

#### Discussion

Provide a custom stage if you have custom code for determining search results. For example, you might use a custom stage to provide the Spotlight search tool with app-managed relevance scores. The tool makes your custom stages available to the model, which determines whether to run them based on the prompt.

For more information about creating a custom stage, see [`Making your indexed content available to Foundation Models`](making-your-indexed-content-available-to-foundation-models.md).

## See Also

- [var guide: SpotlightSearchTool.Guide?](spotlightsearchtool/configuration-swift.struct/guide.md)
  Options you use to guide the search process that the tool uses to retrieve results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/configuration-swift.struct/customstages)*