# enabledFramings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of framings that the monitor is allowed to suggest.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var enabledFramings: [AVCaptureFraming] { get set }
```

```objc
@property (nonatomic, copy) NSArray<AVCaptureFraming *> * enabledFramings;
```

## Mentions

- [Adopting smart framing in your camera app](../adopting-smart-framing-in-your-camera-app.md)

## Discussion

The monitor is capable of recommending any of the framings in the [`supportedFramings`](./supportedframings.md) array. This property contains the subset of [`supportedFramings`](./supportedframings.md) you would like to have recommended to you. You may set this property at any time while running your [`AVCaptureSession`](../avcapturesession.md). This property’s default value is the empty array.

## See Also

### Configuring framings
- [var supportedFramings: [AVCaptureFraming]](./supportedframings.md)
  An array of framings supported by the monitor in its current configuration.
- [var recommendedFraming: AVCaptureFraming?](./recommendedframing.md)
  The latest recommended framing from the monitor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/enabledframings)*