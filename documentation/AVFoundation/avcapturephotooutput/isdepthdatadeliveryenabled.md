# isDepthDataDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether to configure the capture pipeline for depth data capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isDepthDataDeliveryEnabled: Bool { get set }
```

#### Discussion

Depth data captures a per-pixel map of scene depth information delivered alongside the photo image and optionally embedded in image file output. Depth data can be used for purposes such as applying depth-sensitive photo filter effects (like that seen in the iOS Camera app’s Portrait mode) and performing computer vision tasks.

Capturing depth data requires that a capture session set up its internal rendering pipeline differently. If you intend to capture depth data at all, set this property to [`true`](https://developer.apple.com/documentation/Swift/true) before calling the [`AVCaptureSession`](avcapturesession.md) [`startRunning()`](avcapturesession/startrunning().md) method. Changing this property while the session is running requires a lengthy reconfiguration of the capture render pipeline: Live Photo captures in progress will end immediately, unfulfilled photo requests will abort, and video preview will temporarily freeze.

You must enable this option before initiating a photo capture with the [`isDepthDataDeliveryEnabled`](avcapturephotosettings/isdepthdatadeliveryenabled.md) property of your photo settings object set to [`true`](https://developer.apple.com/documentation/Swift/true). However, after you’ve enabled this option, you are free to issue photo capture requests both with and without depth data.

## See Also

- [var isDepthDataDeliverySupported: Bool](avcapturephotooutput/isdepthdatadeliverysupported.md)
  A Boolean value indicating whether the capture output currently supports depth data capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdepthdatadeliveryenabled)*