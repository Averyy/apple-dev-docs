# setExposureTargetBias(_:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Sets the bias to apply to the target exposure value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setExposureTargetBias(_ bias: Float) async -> CMTime
```

#### Discussion

Before changing the value the lens position, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

## Parameters

- `bias`: The bias to apply to the exposure target value.
- `handler`: A callback the system invokes when the adjustment to the exposure target bias is complete. If you call this method multiple times, the system calls the completion handlers in FIFO order. The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [`synchronizationClock`](avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md). You can pass `nil` for this parameter if you don’t require this information.

## See Also

- [var exposureTargetOffset: Float](avcapturedevice/exposuretargetoffset.md)
  The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [var exposureTargetBias: Float](avcapturedevice/exposuretargetbias.md)
  The bias to apply to the target exposure value, in exposure value (EV) units.
- [var minExposureTargetBias: Float](avcapturedevice/minexposuretargetbias.md)
  The minimum supported exposure bias, in exposure value (EV) units.
- [var maxExposureTargetBias: Float](avcapturedevice/maxexposuretargetbias.md)
  The maximum supported exposure bias, in exposure value (EV) units.
- [class let currentExposureTargetBias: Float](avcapturedevice/currentexposuretargetbias.md)
  A special constant that represents the current exposure bias value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setexposuretargetbias(_:completionhandler:))*