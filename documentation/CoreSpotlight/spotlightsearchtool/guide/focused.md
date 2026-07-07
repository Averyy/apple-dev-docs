# focused(_:)

**Framework**: Core Spotlight  
**Kind**: method

A guide that searches only the specified content domain using a compact, on-device-friendly schema.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func focused(_ domain: SpotlightSearchTool.ContentDomain = .items) -> SpotlightSearchTool.Guide
```

## Parameters

- `domain`: The content domain to focus on. Defaults to [`items`](spotlightsearchtool/contentdomain/items-swift.type.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guide/focused(_:))*