# recommendedFraming

**Framework**: AVFoundation  
**Kind**: property

The latest recommended framing from the monitor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var recommendedFraming: AVCaptureFraming? { get }
```

## Mentions

- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md)

#### Discussion

While your [`AVCaptureSession`](avcapturesession.md) is running, the monitor continuously observes its device’s scene to recommend the best framing. This recommended framing is always one of the values in [`enabledFramings`](avcapturesmartframingmonitor/enabledframings.md). This property may return `nil` if smart framing isn’t supported for the device in its current configuration. Its default value is `nil`. This property is key-value observable, and when you observe a change, you may respond to the new recommendation by calling [`setDynamicAspectRatio(_:completionHandler:)`](avcapturedevice/setdynamicaspectratio(_:completionhandler:).md) and setting [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) on the associated device in whatever order best matches your animation between old and new framings.

## See Also

- [var supportedFramings: [AVCaptureFraming]](avcapturesmartframingmonitor/supportedframings.md)
  An array of framings supported by the monitor in its current configuration.
- [var enabledFramings: [AVCaptureFraming]](avcapturesmartframingmonitor/enabledframings.md)
  An array of framings that the monitor is allowed to suggest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/recommendedframing)*