# activeDepthDataFormat

**Framework**: AVFoundation  
**Kind**: property

The currently active depth data format of the capture device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var activeDepthDataFormat: AVCaptureDevice.Format? { get set }
```

## Mentions

- [Capturing photos with depth](capturing-photos-with-depth.md)

#### Discussion

You must obtain exclusive access to the device by calling [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) before setting this property value.

You can set this property only to formats present in the active format’s [`supportedDepthDataFormats`](avcapturedevice/format/supporteddepthdataformats.md) array. Attempting to set an unsupported format throws an exception.

You can’t set the frame rate of depth data directly. Instead, the system synchronizes the depth data frame rate to the device’s [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) and [`activeVideoMaxFrameDuration`](avcapturedevice/activevideomaxframeduration.md) values. It may match the device’s current frame rate, or lower, if the system can’t produce depth data fast enough for the active video frame rate.

Delivery of depth data to a [`AVCaptureDepthDataOutput`](avcapturedepthdataoutput.md) may increase the system load, resulting in a reduced video frame rate for thermal sustainability.

On devices where depth data isn’t supported, this property value is `nil`.

This property is key-value observable.

## See Also

- [var formats: [AVCaptureDevice.Format]](avcapturedevice/formats.md)
  The capture formats a device supports.
- [var activeFormat: AVCaptureDevice.Format](avcapturedevice/activeformat.md)
  The capture format in use by the device.
- [AVCaptureDevice.Format](avcapturedevice/format.md)
  A class that defines media formats and capture settings that capture devices support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activedepthdataformat)*