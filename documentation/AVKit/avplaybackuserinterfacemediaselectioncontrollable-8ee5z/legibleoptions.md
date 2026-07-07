# legibleOptions

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

Array of available subtitle and caption track options.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var legibleOptions: [AVPlaybackUserInterfaceMediaSelectionOption] { get }
```

#### Discussion

This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/legibleoptions)*