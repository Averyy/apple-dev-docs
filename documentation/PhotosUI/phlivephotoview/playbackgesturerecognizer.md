# playbackGestureRecognizer

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

A gesture recognizer that controls playback of the Live Photo in the view.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var playbackGestureRecognizer: UIGestureRecognizer { get }
```

```objc
@property (nonatomic, strong, readonly) UIGestureRecognizer * playbackGestureRecognizer;
```

## Mentions

- [Displaying Live Photos](../../PhotoKit/displaying-live-photos.md)

## Discussion

The Live Photo view automatically creates and installs this gesture recognizer. Use this property to customize the gesture recognizer’s behavior. For example, you might use it in delegate methods that affect how it interacts with other gesture recognizers, or install it on a different view to ensure proper event handling in your app’s view hierarchy.

## See Also

### Managing Playback
- [var isMuted: Bool](./ismuted.md)
  A Boolean value that determines whether the view plays the audio content of its Live Photo.
- [var audioVolume: Float](./audiovolume.md)
  The audio gain to apply to the Live Photo’s movie content during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoview/playbackgesturerecognizer)*