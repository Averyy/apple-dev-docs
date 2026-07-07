# artworkRepresentations

**Framework**: AVKit  
**Kind**: property

Array of available artwork representations in various formats and sizes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var artworkRepresentations: [AVPlaybackUserInterfaceContentArtwork]
```

#### Discussion

Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/artworkrepresentations)*