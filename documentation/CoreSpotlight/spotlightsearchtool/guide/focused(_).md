# focused(_:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Type Method

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

- `domain`: The content domain to focus on. Defaults to [`items`](../contentdomain/items-swift.type.property.md).

## See Also

### Setting the guidance levels
- [static var complete: SpotlightSearchTool.Guide](./complete.md)
  A guide that uses all available search techniques.
- [static func dynamic(SpotlightSearchTool.GuidanceProfile) -> SpotlightSearchTool.Guide](./dynamic%28_%29.md)
  A guide that includes only the search techniques specified by the given profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guide/focused(_:))*