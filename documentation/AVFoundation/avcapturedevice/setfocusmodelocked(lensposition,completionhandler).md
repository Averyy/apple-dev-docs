# setFocusModeLocked(lensPosition:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Locks the lens position at the specified value, and sets the focus mode to a locked state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setFocusModeLocked(lensPosition: Float) async -> CMTime
```

#### Discussion

Calling this method is the only way to set the value of the [`lensPosition`](avcapturedevice/lensposition.md) property. This method throws an exception if you set the value to an unsupported level.

Before changing the value the lens position, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

## Parameters

- `lensPosition`: The lens position. Pass a value of [`currentLensPosition`](avcapturedevice/currentlensposition.md) to leave the current lens position unchanged.
- `handler`: A callback the system invokes when the adjustment to the lens position is complete and the [`focusMode`](avcapturedevice/focusmode-swift.property.md) set to a locked state. If you call this method multiple times, the system calls the completion handlers in FIFO order. The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [`synchronizationClock`](avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md). You can pass `nil` for this parameter if you don’t require this information.

## See Also

- [var isLockingFocusWithCustomLensPositionSupported: Bool](avcapturedevice/islockingfocuswithcustomlenspositionsupported.md)
  A Boolean value that indicates whether the device supports locking focus to a specific lens position.
- [var lensPosition: Float](avcapturedevice/lensposition.md)
  The current focus position of the lens.
- [class let currentLensPosition: Float](avcapturedevice/currentlensposition.md)
  A constant that represents the current lens position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setfocusmodelocked(lensposition:completionhandler:))*