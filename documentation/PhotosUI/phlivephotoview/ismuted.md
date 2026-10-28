# isMuted

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view plays the audio content of its Live Photo.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isMuted: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite, getter=isMuted) BOOL muted;
```

## Discussion

The default value is `false`, indicating that the view plays audio content along with the motion content of its Live Photo. Change this value to `true` to play motion content but not audio content.

## See Also

### Managing Playback
- [var playbackGestureRecognizer: UIGestureRecognizer](./playbackgesturerecognizer.md)
  A gesture recognizer that controls playback of the Live Photo in the view.
- [var audioVolume: Float](./audiovolume.md)
  The audio gain to apply to the Live Photo’s movie content during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoview/ismuted)*