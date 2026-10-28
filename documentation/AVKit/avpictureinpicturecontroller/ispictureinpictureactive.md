# isPictureInPictureActive

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the Picture in Picture window is onscreen.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isPictureInPictureActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPictureInPictureActive) BOOL pictureInPictureActive;
```

## Discussion

This property is key-value observable.

## See Also

### Accessing Picture in Picture state
- [class func isPictureInPictureSupported() -> Bool](./ispictureinpicturesupported%28%29.md)
  Returns a Boolean value that indicates whether the current device supports Picture in Picture.
- [var isPictureInPicturePossible: Bool](./ispictureinpicturepossible.md)
  A Boolean value that indicates whether Picture in Picture playback is currently possible.
- [var isPictureInPictureSuspended: Bool](./ispictureinpicturesuspended.md)
  A Boolean value that indicates whether the system suspends the controller’s Picture in Picture window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/ispictureinpictureactive)*