# audioVolume

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The audio gain to apply to the Live Photo’s movie content during playback.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var audioVolume: Float { get set }
```

```objc
@property (nonatomic, assign, readwrite) float audioVolume;
```

## Discussion

Values for this property must be between `0.0` and `1.0`, inclusive. A value of `1.0` (the default) plays audio content from the Live Photo at full volume (relative to the system volume). A value of `0.0` is equivalent to setting the [`isMuted`](./ismuted.md) property to `true`.

## See Also

### Managing Playback
- [var playbackGestureRecognizer: UIGestureRecognizer](./playbackgesturerecognizer.md)
  A gesture recognizer that controls playback of the Live Photo in the view.
- [var isMuted: Bool](./ismuted.md)
  A Boolean value that determines whether the view plays the audio content of its Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoview/audiovolume)*