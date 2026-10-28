# startPictureInPicture()

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Starts Picture in Picture, if possible.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func startPictureInPicture()
```

```objc
- (void) startPictureInPicture;
```

## Mentions

- [Adopting Picture in Picture for video calls](../adopting-picture-in-picture-for-video-calls.md)

## Discussion

When you call this method and Picture in Picture (PiP) is possible, your delegate receives a call to its [`pictureInPictureControllerWillStartPictureInPicture(_:)`](../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture%28_%29.md) method. After a successful start, your delegate receives a call to the [`pictureInPictureControllerDidStartPictureInPicture(_:)`](../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture%28_%29.md) method.

If PiP fails, your delegate receives a call to the [`pictureInPictureController(_:failedToStartPictureInPictureWithError:)`](../avpictureinpicturecontrollerdelegate/pictureinpicturecontroller%28_,failedtostartpictureinpicturewitherror%29.md)method.

Whether you explicitly stop PiP, the user stops it through interaction, or the system stops it, your delegate receives a call to the [`pictureInPictureControllerWillStopPictureInPicture(_:)`](../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture%28_%29.md) method, followed by the [`pictureInPictureControllerDidStopPictureInPicture(_:)`](../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture%28_%29.md) method after the PiP stop animation completes.

## See Also

### Controlling Picture in Picture playback
- [var canStopPictureInPicture: Bool](./canstoppictureinpicture.md)
  A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [var canStartPictureInPictureAutomaticallyFromInline: Bool](./canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [func stopPictureInPicture()](./stoppictureinpicture%28%29.md)
  Stops Picture in Picture, if active.
- [func invalidatePlaybackState()](./invalidateplaybackstate%28%29.md)
  Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/startpictureinpicture())*