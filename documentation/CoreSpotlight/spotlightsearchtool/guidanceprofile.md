# SpotlightSearchTool.GuidanceProfile

**Framework**: Core Spotlight  
**Kind**: struct

Options for which techniques to use to determine a match.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct GuidanceProfile
```

#### Overview

When you configure the [`SpotlightSearchTool`](spotlightsearchtool.md) with the [`SpotlightSearchTool.GuidanceLevel.dynamic(_:)`](spotlightsearchtool/guidancelevel/dynamic(_:).md) guidance option, you provide an instance of this structure. Configure the structure with the search techniques you want to allow or disallow, and might do so to prevent searches using techniques that don’t apply to your content. If you don’t specify a value for a property, the tool doesn’t use that search option.

In addition to specifying what types of searches to perform, you can also specify which of your content’s attributes to consider when looking for matches. The default behavior searches all of the attributes present for your content, but you can specify a custom set of attributes if you want the tool to ignore certain values.

## Topics

### Creating the guidance profile
- [init(textMatch: Bool?, similarityMatch: Bool?, numericMatch: Bool?, dates: Bool?, people: Bool?, contentType: Bool?, attributes: [SearchableItemAttribute]?)](spotlightsearchtool/guidanceprofile/init(textmatch:similaritymatch:numericmatch:dates:people:contenttype:attributes:).md)
### Specifying the supported search techniques
- [var contentType: Bool?](spotlightsearchtool/guidanceprofile/contenttype.md)
  A Boolean value that indicates whether to determine matches using an item’s type.
- [var dates: Bool?](spotlightsearchtool/guidanceprofile/dates.md)
  A Boolean value that indicates whether to determine matches using date or time values.
- [var numericMatch: Bool?](spotlightsearchtool/guidanceprofile/numericmatch.md)
  A Boolean value that indicates whether to determine matches using numerical values.
- [var people: Bool?](spotlightsearchtool/guidanceprofile/people.md)
  A Boolean value that indicates whether to determine matches using the presence of specific people.
- [var similarityMatch: Bool?](spotlightsearchtool/guidanceprofile/similaritymatch.md)
  A Boolean value that indicates whether to perform semantic similarity matching on your content.
- [var textMatch: Bool?](spotlightsearchtool/guidanceprofile/textmatch.md)
  A Boolean value that indicates whether to perform keyword-based text matching on your content.
### Getting the relevant attributes
- [var attributes: [SearchableItemAttribute]?](spotlightsearchtool/guidanceprofile/attributes.md)
  The relevant attributes from your content that you want to search.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let configuration: SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.property.md)
  The configuration details for the search tool.
- [SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.
- [SpotlightSearchTool.Guide](spotlightsearchtool/guide.md)
  A type you use to offer guidance about what search capabillities to employ during a session.
- [SpotlightSearchTool.GuidanceLevel](spotlightsearchtool/guidancelevel.md)
  Options for how to search your app’s content.
- [SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain.md)
  A content domain that defines which fields and attribute mappings are presented to the model during a focused search session.
- [SpotlightSearchTool.FormatLevel](spotlightsearchtool/formatlevel.md)
  Controls how tool responses are serialized for the model’s context window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidanceprofile)*