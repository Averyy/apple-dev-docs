# SpotlightSearchTool.Guide

**Framework**: Core Spotlight  
**Kind**: struct

A type you use to offer guidance about what search capabillities to employ during a session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Guide
```

#### Overview

Use this type to specify additional guidance about how you want the model to search your content. At configuration time, configure an instance of this structure and assign it to the [`guide`](spotlightsearchtool/configuration-swift.struct/guide.md) property of your configuration object. You use guidance options primarily to limit the types of searches the model performs or to scope searches to specific types of content. Adding guidance can help improve the efficiency of searches, especially if you eliminate search techniques that don’t apply to your content.

## Topics

### Creating the search tool
- [init(level: SpotlightSearchTool.GuidanceLevel, format: SpotlightSearchTool.FormatLevel)](spotlightsearchtool/guide/init(level:format:).md)
### Getting the guidance
- [let format: SpotlightSearchTool.FormatLevel](spotlightsearchtool/guide/format.md)
  The representation format for tool responses returned to the model.
- [let level: SpotlightSearchTool.GuidanceLevel](spotlightsearchtool/guide/level.md)
  The guidance for the model to use during a session.
### Type Properties
- [static var complete: SpotlightSearchTool.Guide](spotlightsearchtool/guide/complete.md)
  A guide that uses all available search techniques.
### Type Methods
- [static func dynamic(SpotlightSearchTool.GuidanceProfile) -> SpotlightSearchTool.Guide](spotlightsearchtool/guide/dynamic(_:).md)
  A guide that includes only the search techniques specified by the given profile.
- [static func focused(SpotlightSearchTool.ContentDomain) -> SpotlightSearchTool.Guide](spotlightsearchtool/guide/focused(_:).md)
  A guide that searches only the specified content domain using a compact, on-device-friendly schema.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let configuration: SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.property.md)
  The configuration details for the search tool.
- [SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.
- [SpotlightSearchTool.GuidanceProfile](spotlightsearchtool/guidanceprofile.md)
  Options for which techniques to use to determine a match.
- [SpotlightSearchTool.GuidanceLevel](spotlightsearchtool/guidancelevel.md)
  Options for how to search your app’s content.
- [SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain.md)
  A content domain that defines which fields and attribute mappings are presented to the model during a focused search session.
- [SpotlightSearchTool.FormatLevel](spotlightsearchtool/formatlevel.md)
  Controls how tool responses are serialized for the model’s context window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guide)*