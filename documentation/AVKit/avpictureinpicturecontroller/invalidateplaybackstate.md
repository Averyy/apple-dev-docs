# invalidatePlaybackState()

**Framework**: AVKit  
**Kind**: method

Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func invalidatePlaybackState()
```

#### Discussion

Call this method whenever you start or pause playback and when the underlying content duration changes.

## See Also

- [var canStopPictureInPicture: Bool](avpictureinpicturecontroller/canstoppictureinpicture.md)
  A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [var canStartPictureInPictureAutomaticallyFromInline: Bool](avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [func startPictureInPicture()](avpictureinpicturecontroller/startpictureinpicture.md)
  Starts Picture in Picture, if possible.
- [func stopPictureInPicture()](avpictureinpicturecontroller/stoppictureinpicture.md)
  Stops Picture in Picture, if active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/invalidateplaybackstate())*