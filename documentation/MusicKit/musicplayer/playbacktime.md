# playbackTime

**Framework**: MusicKit  
**Kind**: property

The current playback time, in seconds, of the current entry.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var playbackTime: TimeInterval { get set }
```

#### Discussion

Changing the value of this property moves the playhead to the new location. For content streaming live from a server, this value represents the time from the beginning of the playlist when it first loads. This property returns `NaN` if the [`CMTime`](https://developer.apple.com/documentation/CoreMedia/CMTime) is invalid or indefinite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/playbacktime)*