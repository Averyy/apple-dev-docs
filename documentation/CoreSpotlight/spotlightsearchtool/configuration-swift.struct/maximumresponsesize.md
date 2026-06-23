# maximumResponseSize

**Framework**: Core Spotlight  
**Kind**: property

The maximum number of UTF-8 characters of rendered tool output the search tool sends back to the model on a single call.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var maximumResponseSize: Int?
```

#### Discussion

If `nil`, the tool picks a default based on the configured [`guide`](spotlightsearchtool/configuration-swift.struct/guide.md). Pass an explicit value to override that default; the override applies regardless of the guide’s level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/configuration-swift.struct/maximumresponsesize)*