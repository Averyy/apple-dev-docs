# setDynamicAspectRatio(_:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Updates the dynamic aspect ratio of the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func setDynamicAspectRatio(_ dynamicAspectRatio: AVCaptureDevice.AspectRatio) async throws -> CMTime
```

#### Discussion

This is the only way of setting [`dynamicAspectRatio`](avcapturedevice/dynamicaspectratio.md). This method throws an `NSInvalidArgumentException` if `dynamicAspectRatio` is not a supported aspect ratio found in the device’s activeFormat’s [`supportedDynamicAspectRatios`](avcapturedevice/format/supporteddynamicaspectratios.md). This method throws an `NSGenericException` if you call it without first obtaining exclusive access to the device using [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md).

## Parameters

- `dynamicAspectRatio`: The new   the device should output.
- `handler`: A block called by the device when   is set to the value specified. If you call   multiple times, the completion handlers are called in FIFO order. The block receives a timestamp which matches that of the first buffer to which all settings have been applied. Note that the timestamp is synchronized to the device clock, and thus must be converted to the   prior to comparison with the timestamps of buffers delivered via an  . You may pass   for the   parameter if you do not need to know when the operation completes.

## See Also

- [AVCaptureDevice.AspectRatio](avcapturedevice/aspectratio.md)
  String constants describing the different video aspect ratios you can configure for a particular device.
- [var dynamicAspectRatio: AVCaptureDevice.AspectRatio?](avcapturedevice/dynamicaspectratio.md)
  A key-value observable property indicating the current aspect ratio for a device.
- [var dynamicDimensions: CMVideoDimensions](avcapturedevice/dynamicdimensions.md)
  A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setdynamicaspectratio(_:completionhandler:))*