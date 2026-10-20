# setFocusModeLocked(lensPosition:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Locks the lens position at the specified value, and sets the focus mode to a locked state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setFocusModeLocked(lensPosition: Float, completionHandler handler: (@Sendable (CMTime) -> Void)? = nil)
```

```swift
func setFocusModeLocked(lensPosition: Float) async -> CMTime
```

```objc
- (void) setFocusModeLockedWithLensPosition:(float) lensPosition completionHandler:(void (^)(CMTime syncTime)) handler;
```

#### Discussion

Calling this method is the only way to set the value of the [`lensPosition`](./lensposition.md) property. This method throws an exception if you set the value to an unsupported level.

Before changing the value the lens position, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

## Parameters

- `lensPosition`: The lens position. Pass a value of [`currentLensPosition`](./currentlensposition.md) to leave the current lens position unchanged.
- `handler`: A callback the system invokes when the adjustment to the lens position is complete and the [`focusMode`](./focusmode-swift.property.md) set to a locked state. If you call this method multiple times, the system calls the completion handlers in FIFO order.

  The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [`synchronizationClock`](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md).

  You can pass `nil` for this parameter if you don’t require this information.

## See Also

### Setting focus manually
- [var isLockingFocusWithCustomLensPositionSupported: Bool](./islockingfocuswithcustomlenspositionsupported.md)
  A Boolean value that indicates whether the device supports locking focus to a specific lens position.
- [var lensPosition: Float](./lensposition.md)
  The current focus position of the lens.
- [class let currentLensPosition: Float](./currentlensposition.md)
  A constant that represents the current lens position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setfocusmodelocked(lensposition:completionhandler:))*