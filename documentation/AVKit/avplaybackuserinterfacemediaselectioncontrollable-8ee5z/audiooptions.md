# audioOptions

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

Array of available audio track options.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var audioOptions: [AVPlaybackUserInterfaceMediaSelectionOption] { get }
```

#### Discussion

This includes all audio streams provided by the media source such as different languages, director’s commentary, and alternative audio mixes. Options are ordered by preference with the primary language or default audio track typically appearing first. May be empty for content without selectable audio options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiooptions)*