# isDualCameraDualPhotoDeliverySupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var isDualCameraDualPhotoDeliverySupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isDualCameraDualPhotoDeliverySupported) BOOL dualCameraDualPhotoDeliverySupported;
```

#### Discussion

Not all devices and capture formats support dual camera capture. This property’s value can change if the [`sessionPreset`](../avcapturesession/sessionpreset.md) property of the current capture session or the [`activeFormat`](../avcapturedevice/activeformat.md) property of the underlying capture device changes. If a camera or format change causes this property’s value to become [`false`](../../Swift/false.md), the [`isDualCameraDualPhotoDeliveryEnabled`](./isdualcameradualphotodeliveryenabled.md) property’s value also becomes [`false`](../../Swift/false.md).

This property is key-value observable.

## See Also

### Configuring dual camera capture
- [var isDualCameraFusionSupported: Bool](./isdualcamerafusionsupported.md)
  A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device.
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](./isdualcameradualphotodeliveryenabled.md)
  A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliverysupported)*