# lensPosition

**Framework**: AVFoundation  
**Kind**: property

The current focus position of the lens.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var lensPosition: Float { get }
```

#### Discussion

A lens position value doesn’t correspond to an exact physical distance, nor does it represent a consistent focus distance from device to device.

The range of possible positions is `0.0` to `1.0`, with `0.0` being the shortest distance at which the lens can focus and `1.0` the furthest. Note that `1.0` doesn’t represent focus at infinity. The default value is `1.0`.

This property is key-value observable.

## See Also

- [var isLockingFocusWithCustomLensPositionSupported: Bool](avcapturedevice/islockingfocuswithcustomlenspositionsupported.md)
  A Boolean value that indicates whether the device supports locking focus to a specific lens position.
- [class let currentLensPosition: Float](avcapturedevice/currentlensposition.md)
  A constant that represents the current lens position.
- [func setFocusModeLocked(lensPosition: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setfocusmodelocked(lensposition:completionhandler:).md)
  Locks the lens position at the specified value, and sets the focus mode to a locked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/lensposition)*