# setExposureTargetBias(_:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the bias to apply to the target exposure value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setExposureTargetBias(_ bias: Float, completionHandler handler: (@Sendable (CMTime) -> Void)? = nil)
```

```swift
func setExposureTargetBias(_ bias: Float) async -> CMTime
```

```objc
- (void) setExposureTargetBias:(float) bias completionHandler:(void (^)(CMTime syncTime)) handler;
```

## Discussion

Before changing the value the lens position, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

## Parameters

- `bias`: The bias to apply to the exposure target value.
- `handler`: A callback the system invokes when the adjustment to the exposure target bias is complete. If you call this method multiple times, the system calls the completion handlers in FIFO order.

  The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [`synchronizationClock`](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md).

  You can pass `nil` for this parameter if you don’t require this information.

## See Also

### Adjusting exposure compensation
- [var exposureTargetOffset: Float](./exposuretargetoffset.md)
  The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [var exposureTargetBias: Float](./exposuretargetbias.md)
  The bias to apply to the target exposure value, in exposure value (EV) units.
- [var minExposureTargetBias: Float](./minexposuretargetbias.md)
  The minimum supported exposure bias, in exposure value (EV) units.
- [var maxExposureTargetBias: Float](./maxexposuretargetbias.md)
  The maximum supported exposure bias, in exposure value (EV) units.
- [class let currentExposureTargetBias: Float](./currentexposuretargetbias.md)
  A special constant that represents the current exposure bias value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setexposuretargetbias(_:completionhandler:))*