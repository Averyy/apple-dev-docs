# allowsPictureInPicturePlayback

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the player view allows Picture in Picture playback.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var allowsPictureInPicturePlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsPictureInPicturePlayback;
```

## Discussion

The default value is `false`.

## See Also

### Configuring picture in picture
- [var pictureInPictureDelegate: (any AVPlayerViewPictureInPictureDelegate)?](./pictureinpicturedelegate.md)
  The Picture in Picture delegate object.
- [protocol AVPlayerViewPictureInPictureDelegate](../avplayerviewpictureinpicturedelegate.md)
  A protocol that defines the methods to implement to respond to Picture in Picture playback events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/allowspictureinpictureplayback)*