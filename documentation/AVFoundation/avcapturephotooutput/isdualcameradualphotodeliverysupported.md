# isDualCameraDualPhotoDeliverySupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isDualCameraDualPhotoDeliverySupported: Bool { get }
```

#### Discussion

Not all devices and capture formats support dual camera capture. This property’s value can change if the [`sessionPreset`](avcapturesession/sessionpreset.md) property of the current capture session or the [`activeFormat`](avcapturedevice/activeformat.md) property of the underlying capture device changes. If a camera or format change causes this property’s value to become [`false`](https://developer.apple.com/documentation/swift/false), the [`isDualCameraDualPhotoDeliveryEnabled`](avcapturephotooutput/isdualcameradualphotodeliveryenabled.md) property’s value also becomes [`false`](https://developer.apple.com/documentation/swift/false).

This property is key-value observable.

## See Also

- [var isDualCameraFusionSupported: Bool](avcapturephotooutput/isdualcamerafusionsupported.md)
  A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device.
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](avcapturephotooutput/isdualcameradualphotodeliveryenabled.md)
  A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliverysupported)*