# exitsFullScreenWhenPlaybackEnds

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the player exits full-screen mode when playback ends.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var exitsFullScreenWhenPlaybackEnds: Bool { get set }
```

#### Discussion

If you enqueue multiple player items, the player exits full-screen mode after it plays all remaining items in the queue.

The default value is `false`.

## See Also

- [var entersFullScreenWhenPlaybackBegins: Bool](avplayerviewcontroller/entersfullscreenwhenplaybackbegins.md)
  A Boolean value that determines whether the player automatically displays in full screen when the user taps the play button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/exitsfullscreenwhenplaybackends)*