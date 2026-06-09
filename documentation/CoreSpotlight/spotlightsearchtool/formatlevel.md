# SpotlightSearchTool.FormatLevel

**Framework**: Core Spotlight  
**Kind**: enum

Controls how tool responses are serialized for the model’s context window.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum FormatLevel
```

#### Overview

The tool returns search results to the model as part of the generation context. The format level determines how those results are encoded:

- `.structured`: Full encoding with the highest fidelity, highest token cost. Best when the model needs to reason over attribute keys and values precisely (e.g., filtering, re-querying).
- `.compact`: Terse, line-oriented text encoding. Best for models with limited context.

## Topics

### Getting the format levels
- [SpotlightSearchTool.FormatLevel.compact](spotlightsearchtool/formatlevel/compact.md)
  Compact encoding
- [SpotlightSearchTool.FormatLevel.structured](spotlightsearchtool/formatlevel/structured.md)
  Full, structured encoded

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let configuration: SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.property.md)
  The configuration details for the search tool.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/formatlevel)*