# affectsListeningHistory

**Framework**: MusicKit  
**Kind**: property

A Boolean value that indicates whether this playing this queue will affect the user’s listening history. Defaults to `true`.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
var affectsListeningHistory: Bool { get set }
```

#### Discussion

If `false`, or the user has Settings > Music > Use Listening History set to off, this queue will not show up in the Music app’s Recently Played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue/affectslisteninghistory)*