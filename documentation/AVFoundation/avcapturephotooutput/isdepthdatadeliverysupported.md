# isDepthDataDeliverySupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the capture output currently supports depth data capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isDepthDataDeliverySupported: Bool { get }
```

#### Discussion

Depth data captures a per-pixel map of scene depth information delivered alongside the photo image and optionally embedded in image file output. Depth data can be used for purposes such as applying depth-sensitive photo filter effects (like that seen in the iOS Camera app’s Portrait mode) and performing computer vision tasks.

Not all devices and capture formats support depth capture. This property’s value can change if the [`sessionPreset`](avcapturesession/sessionpreset.md) property of the current capture session or the [`activeFormat`](avcapturedevice/activeformat.md) property of the underlying capture device changes. If a camera or format change causes this property’s value to become [`false`](https://developer.apple.com/documentation/swift/false), the [`isDepthDataDeliveryEnabled`](avcapturephotooutput/isdepthdatadeliveryenabled.md) property’s value also becomes [`false`](https://developer.apple.com/documentation/swift/false).

This property is key-value observable.

## See Also

- [var isDepthDataDeliveryEnabled: Bool](avcapturephotooutput/isdepthdatadeliveryenabled.md)
  A Boolean value that specifies whether to configure the capture pipeline for depth data capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdepthdatadeliverysupported)*