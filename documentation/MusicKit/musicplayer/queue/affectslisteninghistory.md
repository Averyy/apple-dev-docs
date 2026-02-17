# affectsListeningHistory

**Framework**: MusicKit  
**Kind**: property

A Boolean value that indicates whether this playing this queue will affect the user’s listening history. Defaults to `true`.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
var affectsListeningHistory: Bool { get set }
```

#### Discussion

If `false`, or the user has Settings > Music > Use Listening History set to off, this queue will not show up in the Music app’s Recently Played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue/affectslisteninghistory)*