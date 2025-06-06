# allowsPictureInPicturePlayback

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the player allows Picture in Picture playback.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsPictureInPicturePlayback: Bool { get set }
```

#### Discussion

Set this value to [`false`](https://developer.apple.com/documentation/swift/false) to disable Picture in Picture playback. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var canStartPictureInPictureAutomaticallyFromInline: Bool](avplayerviewcontroller/canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when transitioning to the background when the view controller presents its content inline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/allowspictureinpictureplayback)*