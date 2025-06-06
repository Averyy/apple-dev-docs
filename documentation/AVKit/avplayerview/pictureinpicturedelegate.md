# pictureInPictureDelegate

**Framework**: AVKit  
**Kind**: property

The Picture in Picture delegate object.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
weak var pictureInPictureDelegate: (any AVPlayerViewPictureInPictureDelegate)? { get set }
```

## See Also

- [var allowsPictureInPicturePlayback: Bool](avplayerview/allowspictureinpictureplayback.md)
  A Boolean value that determines whether the player view allows Picture in Picture playback.
- [protocol AVPlayerViewPictureInPictureDelegate](avplayerviewpictureinpicturedelegate.md)
  A protocol that defines the methods to implement to respond to Picture in Picture playback events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/pictureinpicturedelegate)*