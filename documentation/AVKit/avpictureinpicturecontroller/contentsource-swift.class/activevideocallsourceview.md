# activeVideoCallSourceView

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The view that contains the video content of the call.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var activeVideoCallSourceView: UIView? { get }
```

```objc
@property (nonatomic, weak, readonly) UIView * activeVideoCallSourceView;
```

#### Discussion

The controller uses this view’s layout frame and visibility to determine whether or not Picture in Picture begins automatically when the app moves to the background. The view’s layout frame also influences the animation when entering and exiting Picture in Picture.

## See Also

### Accessing the active call presentation
- [var activeVideoCallContentViewController: AVPictureInPictureVideoCallViewController](./activevideocallcontentviewcontroller.md)
  The view controller that presents the video call content.
- [class AVPictureInPictureVideoCallViewController](../../avpictureinpicturevideocallviewcontroller.md)
  A view controller that presents content from a video call in Picture in Picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/activevideocallsourceview)*