# stopPlayback(animated:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Stops playback of a Live Photo in an animated manner.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func stopPlayback(animated: Bool)
```

```objc
- (void) stopPlaybackAnimated:(BOOL) animated;
```

## Discussion

Calling this method with a value of `false` is the same as calling [`stopPlayback()`](./stopplayback%28%29.md).

## Parameters

- `animated`: A Boolean value that indicates whether playback stops immediately or with animation.

## See Also

### Manually Playing Live Photo Content
- [func startPlayback(with: PHLivePhotoViewPlaybackStyle)](./startplayback%28with%29.md)
  Begins playback of Live Photo content in the view.
- [func stopPlayback()](./stopplayback%28%29.md)
  Stops playback of a Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoview/stopplayback(animated:))*