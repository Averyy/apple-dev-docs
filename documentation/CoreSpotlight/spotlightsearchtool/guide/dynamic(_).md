# dynamic(_:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Type Method

A guide that includes only the search techniques specified by the given profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func dynamic(_ profile: SpotlightSearchTool.GuidanceProfile) -> SpotlightSearchTool.Guide
```

## Parameters

- `profile`: The set of search techniques and attributes the model may use.

## See Also

### Setting the guidance levels
- [static var complete: SpotlightSearchTool.Guide](./complete.md)
  A guide that uses all available search techniques.
- [static func focused(SpotlightSearchTool.ContentDomain) -> SpotlightSearchTool.Guide](./focused%28_%29.md)
  A guide that searches only the specified content domain using a compact, on-device-friendly schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guide/dynamic(_:))*