# SpotlightSearchTool.Guide

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

A type you use to offer guidance about what search capabillities to employ during a session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Guide
```

## Overview

Use this type to specify additional guidance about how you want the model to search your content. At configuration time, configure an instance of this structure and assign it to the [`guide`](./configuration-swift.struct/guide.md) property of your configuration object. You use guidance options primarily to limit the types of searches the model performs or to scope searches to specific types of content. Adding guidance can help improve the efficiency of searches, especially if you eliminate search techniques that don’t apply to your content.

## Topics

### Creating the search tool
- [init(level: SpotlightSearchTool.GuidanceLevel, format: SpotlightSearchTool.FormatLevel)](./guide/init%28level,format%29.md)
### Getting the guidance
- [let level: SpotlightSearchTool.GuidanceLevel](./guide/level.md)
  The guidance for the model to use during a session.
- [let format: SpotlightSearchTool.FormatLevel](./guide/format.md)
  The representation format for tool responses returned to the model.
### Setting the guidance levels
- [static var complete: SpotlightSearchTool.Guide](./guide/complete.md)
  A guide that uses all available search techniques.
- [static func dynamic(SpotlightSearchTool.GuidanceProfile) -> SpotlightSearchTool.Guide](./guide/dynamic%28_%29.md)
  A guide that includes only the search techniques specified by the given profile.
- [static func focused(SpotlightSearchTool.ContentDomain) -> SpotlightSearchTool.Guide](./guide/focused%28_%29.md)
  A guide that searches only the specified content domain using a compact, on-device-friendly schema.

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
- [SpotlightSearchTool.GuidanceProfile](./guidanceprofile.md)
  Options for which techniques to use to determine a match.
- [SpotlightSearchTool.GuidanceLevel](./guidancelevel.md)
  Options for how to search your app’s content.
- [SpotlightSearchTool.ContentDomain](./contentdomain.md)
  A content domain that defines which fields and attribute mappings are presented to the model during a focused search session.
- [SpotlightSearchTool.FormatLevel](./formatlevel.md)
  Controls how tool responses are serialized for the model’s context window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guide)*