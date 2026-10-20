# stopPictureInPicture()

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Stops Picture in Picture, if active.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func stopPictureInPicture()
```

```objc
- (void) stopPictureInPicture;
```

#### Discussion

Regardless of how Picture in Picture stops, the controller calls the delegate’s [`pictureInPictureControllerWillStopPictureInPicture(_:)`](../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture%28_%29.md) method. When the PiP animation completes, the controller finalizes the session by calling the delegate’s [`pictureInPictureControllerDidStopPictureInPicture(_:)`](../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture%28_%29.md) method.

## See Also

### Controlling Picture in Picture playback
- [var canStopPictureInPicture: Bool](./canstoppictureinpicture.md)
  A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [var canStartPictureInPictureAutomaticallyFromInline: Bool](./canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [func startPictureInPicture()](./startpictureinpicture%28%29.md)
  Starts Picture in Picture, if possible.
- [func invalidatePlaybackState()](./invalidateplaybackstate%28%29.md)
  Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/stoppictureinpicture())*