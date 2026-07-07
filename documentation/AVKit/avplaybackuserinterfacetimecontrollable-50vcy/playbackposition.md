# playbackPosition

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

A snapshot of the current playback position. Must be updated — with a fresh `hostTime` — on play, pause, seek, scan, and buffering state changes. Must be observable.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var playbackPosition: AVPlaybackUserInterfacePlaybackPosition { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/playbackposition)*