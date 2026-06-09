# configuration

**Framework**: Core Spotlight  
**Kind**: property

The configuration details for the search tool.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let configuration: SpotlightSearchTool.Configuration
```

#### Discussion

Use this property to specify the configuration data you want to use with the tool. You use this property to configure the data sources for the tool to search, guidance on how to perform searches, and any custom processing steps your app provides. For more information on how to configure and use [`SpotlightSearchTool`](spotlightsearchtool.md), see [`Making your indexed content available to Foundation Models`](making-your-indexed-content-available-to-foundation-models.md).

## See Also

- [SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.
- [SpotlightSearchTool.Guide](spotlightsearchtool/guide.md)
  A type you use to offer guidance about what search capabillities to employ during a session.
- [SpotlightSearchTool.GuidanceProfile](spotlightsearchtool/guidanceprofile.md)
  Options for which techniques to use to determine a match.
- [SpotlightSearchTool.GuidanceLevel](spotlightsearchtool/guidancelevel.md)
  Options for how to search your app’s content.
- [SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain.md)
  A content domain that defines which fields and attribute mappings are presented to the model during a focused search session.
- [SpotlightSearchTool.FormatLevel](spotlightsearchtool/formatlevel.md)
  Controls how tool responses are serialized for the model’s context window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/configuration-swift.property)*