# SpotlightSearchTool.Configuration

**Framework**: Core Spotlight  
**Kind**: struct

The configuration data to use when creating a Spotlight search tool.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Overview

Use this structure to specify the data sources, guidance, and options for [`SpotlightSearchTool`](spotlightsearchtool.md) to use when performing searches. Create an instance of this structure as part of the setup of the search tool, and configure it with the information you want. For more information about configuring the search tool, see [`Making your indexed content available to Foundation Models`](making-your-indexed-content-available-to-foundation-models.md).

## Topics

### Creating the configuration object
- [init(sources: [SearchSource], guide: SpotlightSearchTool.Guide?, contactResolver: (any ContactResolver)?, customStages: [any CustomStage])](spotlightsearchtool/configuration-swift.struct/init(sources:guide:contactresolver:customstages:).md)
### Configuring the search sources
- [var sources: [SearchSource]](spotlightsearchtool/configuration-swift.struct/sources.md)
  The data sources and options to use during a search.
### Resolving contacts
- [var contactResolver: (any ContactResolver)?](spotlightsearchtool/configuration-swift.struct/contactresolver.md)
  A custom type you use to identify the owner of your app’s data.
### Customizing the output
- [var guide: SpotlightSearchTool.Guide?](spotlightsearchtool/configuration-swift.struct/guide.md)
  Options you use to guide the search process that the tool uses to retrieve results.
- [var customStages: [any CustomStage]](spotlightsearchtool/configuration-swift.struct/customstages.md)
  Custom pipeline stages you use to help the Spotlight search tool generate results.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SpotlightSearchTool](spotlightsearchtool.md)
  A tool you use to make your app’s custom data available to Foundation Models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/configuration-swift.struct)*