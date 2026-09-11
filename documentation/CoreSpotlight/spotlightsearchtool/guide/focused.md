# focused(_:)

**Framework**: Core Spotlight  
**Kind**: method

A guide that searches only the specified content domain using a compact, on-device-friendly schema.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func focused(_ domain: SpotlightSearchTool.ContentDomain = .items) -> SpotlightSearchTool.Guide
```

## Parameters

- `domain`: The content domain to focus on. Defaults to [`items`](spotlightsearchtool/contentdomain/items-swift.type.property.md).

## See Also

- [static var complete: SpotlightSearchTool.Guide](spotlightsearchtool/guide/complete.md)
  A guide that uses all available search techniques.
- [static func dynamic(SpotlightSearchTool.GuidanceProfile) -> SpotlightSearchTool.Guide](spotlightsearchtool/guide/dynamic(_:).md)
  A guide that includes only the search techniques specified by the given profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guide/focused(_:))*