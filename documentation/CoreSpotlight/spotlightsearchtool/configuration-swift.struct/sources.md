# sources

**Framework**: Core Spotlight  
**Kind**: property

The data sources and options to use during a search.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var sources: [SearchSource]
```

#### Discussion

Use this property to specify where you want [`SpotlightSearchTool`](spotlightsearchtool.md) to look for your app’s data. Fill this property with [`CoreSpotlightSource`](corespotlightsource.md) or [`FileSource`](filesource.md) types. If you specify multiple search sources, the tool searches all of them and delivers the merged results to the model. Each source object also has options about how much data to retrieve from the source, which you can use to control how much data you send to the model.

If you don’t specify a value for this property, the search tool uses a default [`CoreSpotlightSource`](corespotlightsource.md) to search your app’s Spotlight index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/configuration-swift.struct/sources)*