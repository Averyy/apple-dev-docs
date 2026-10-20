# canStopPictureInPicture

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether Picture in Picture is active and is able to stop.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
var canStopPictureInPicture: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canStopPictureInPicture;
```

## Mentions

- [Adopting Picture in Picture in a custom player](../adopting-picture-in-picture-in-a-custom-player.md)

#### Discussion

When this value is `true`, calling [`stopPictureInPicture()`](./stoppictureinpicture%28%29.md) stops the active Picture in Picture session. Apps should update the state of UI that starts Picture in Picture when this property value changes.

Thie value is key-value observable.

## See Also

### Controlling Picture in Picture playback
- [var canStartPictureInPictureAutomaticallyFromInline: Bool](./canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [func startPictureInPicture()](./startpictureinpicture%28%29.md)
  Starts Picture in Picture, if possible.
- [func stopPictureInPicture()](./stoppictureinpicture%28%29.md)
  Stops Picture in Picture, if active.
- [func invalidatePlaybackState()](./invalidateplaybackstate%28%29.md)
  Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/canstoppictureinpicture)*