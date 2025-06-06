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

- `lensPosition`: The lens position. Pass a value of   to leave the current lens position unchanged.
- `handler`: You can pass   for this parameter if you don’t require this information.

## See Also

- [var isLockingFocusWithCustomLensPositionSupported: Bool](avcapturedevice/islockingfocuswithcustomlenspositionsupported.md)
  A Boolean value that indicates whether the device supports locking focus to a specific lens position.
- [var lensPosition: Float](avcapturedevice/lensposition.md)
  The current focus position of the lens.
- [class let currentLensPosition: Float](avcapturedevice/currentlensposition.md)
  A constant that represents the current lens position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setfocusmodelocked(lensposition:completionhandler:))*