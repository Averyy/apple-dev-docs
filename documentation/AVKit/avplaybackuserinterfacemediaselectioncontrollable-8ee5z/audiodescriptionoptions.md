# audioDescriptionOptions

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

Array of available audio description track options.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var audioDescriptionOptions: [AVPlaybackUserInterfaceMediaSelectionOption] { get }
```

#### Discussion

Audio description tracks provide narrated descriptions of visual content for visually impaired viewers. Audio description options are distinct from those in [`audioOptions`](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiooptions.md) — they provide a narration layer played alongside the primary audio rather than replacing it. Options are ordered by preference with the primary language or default audio description track typically appearing first. May be empty for content without audio description tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiodescriptionoptions)*