# SpotlightSearchTool.GuidanceLevel.dynamic(_:)

**Framework**: Core Spotlight  
**Kind**: case

An option to search using only the specified techniques.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case dynamic(SpotlightSearchTool.GuidanceProfile)
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Discussion

Choose this option to specify the subset of search techniques to use on your content. The [`SpotlightSearchTool.GuidanceProfile`](spotlightsearchtool/guidanceprofile.md) structure you specify contains properties with the available search techniques. Enable the ones that apply to your app’s content and disable any that don’t apply. For example, if you want to perform only literal searches on strings, enable the [`textMatch`](spotlightsearchtool/guidanceprofile/textmatch.md) property and disable the [`similarityMatch`](spotlightsearchtool/guidanceprofile/similaritymatch.md) property.

## See Also

- [SpotlightSearchTool.GuidanceLevel.complete](spotlightsearchtool/guidancelevel/complete.md)
  An option to use all available search techniques.
- [case focused(SpotlightSearchTool.ContentDomain)](spotlightsearchtool/guidancelevel/focused(_:).md)
  An option to search only specific types of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidancelevel/dynamic(_:))*