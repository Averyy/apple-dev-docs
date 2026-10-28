# startPlayback(with:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Begins playback of Live Photo content in the view.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func startPlayback(with playbackStyle: PHLivePhotoViewPlaybackStyle)
```

```objc
- (void) startPlaybackWithStyle:(PHLivePhotoViewPlaybackStyle) playbackStyle;
```

## Mentions

- [Displaying Live Photos](../../PhotoKit/displaying-live-photos.md)

## Discussion

Use the `playbackStyle` parameter to choose whether to play the full motion and sound content of the Live Photo or only a brief section.

Typically, an app does not need to directly control playback, because a Live Photo view provides interactive playback control. Use this method only when non-interactive playback is appropriate—for example, to briefly animate the content to indicate that a view contains a Live Photo rather than a still image.

## Parameters

- `playbackStyle`: An option for how much of the Live Photo’s motion and sound content to play. See [`PHLivePhotoViewPlaybackStyle`](../phlivephotoviewplaybackstyle.md).

## See Also

### Manually Playing Live Photo Content
- [func stopPlayback()](./stopplayback%28%29.md)
  Stops playback of a Live Photo.
- [func stopPlayback(animated: Bool)](./stopplayback%28animated%29.md)
  Stops playback of a Live Photo in an animated manner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoview/startplayback(with:))*