# supportedFramings

**Framework**: AVFoundation  
**Kind**: property

An array of framings supported by the monitor in its current configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var supportedFramings: [AVCaptureFraming] { get }
```

## Mentions

- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md)

#### Discussion

The monitor is capable of recommending any of the framings in this array. This property is key-value observable and may change as the target capture device’s [`activeFormat`](avcapturedevice/activeformat.md) property changes. This array contains the full set of framings supported by the monitor in the device’s current configuration. You must tell the monitor which smart framings you are interested in having recommended to you by setting the [`enabledFramings`](avcapturesmartframingmonitor/enabledframings.md) property.

## See Also

- [var enabledFramings: [AVCaptureFraming]](avcapturesmartframingmonitor/enabledframings.md)
  An array of framings that the monitor is allowed to suggest.
- [var recommendedFraming: AVCaptureFraming?](avcapturesmartframingmonitor/recommendedframing.md)
  The latest recommended framing from the monitor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/supportedframings)*