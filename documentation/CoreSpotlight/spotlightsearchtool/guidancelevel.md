# SpotlightSearchTool.GuidanceLevel

**Framework**: Core Spotlight  
**Kind**: enum  
**Role**: Enumeration

Options for how to search your app’s content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum GuidanceLevel
```

## Overview

Use this type to guide how the search tool delivers results to the model. You can tell the tool to focus on specific types of content, to search using specific techniques, or to use all available search options.

## Topics

### Getting the guidance levels
- [SpotlightSearchTool.GuidanceLevel.complete](./guidancelevel/complete.md)
  An option to use all available search techniques.
- [case dynamic(SpotlightSearchTool.GuidanceProfile)](./guidancelevel/dynamic%28_%29.md)
  An option to search using only the specified techniques.
- [case focused(SpotlightSearchTool.ContentDomain)](./guidancelevel/focused%28_%29.md)
  An option to search only specific types of content.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the tool behavior
- [let configuration: SpotlightSearchTool.Configuration](./configuration-swift.property.md)
  The configuration details for the search tool.
- [SpotlightSearchTool.Configuration](./configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.
- [SpotlightSearchTool.Guide](./guide.md)
  A type you use to offer guidance about what search capabillities to employ during a session.
- [SpotlightSearchTool.GuidanceProfile](./guidanceprofile.md)
  Options for which techniques to use to determine a match.
- [SpotlightSearchTool.ContentDomain](./contentdomain.md)
  A content domain that defines which fields and attribute mappings are presented to the model during a focused search session.
- [SpotlightSearchTool.FormatLevel](./formatlevel.md)
  Controls how tool responses are serialized for the model’s context window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidancelevel)*