# currentLensPosition

**Framework**: AVFoundation  
**Kind**: property

A constant that represents the current lens position.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class let currentLensPosition: Float
```

#### Discussion

Pass this value to the [`setFocusModeLocked(lensPosition:completionHandler:)`](avcapturedevice/setfocusmodelocked(lensposition:completionhandler:).md) method to lock focus without changing the current lens position.

## See Also

- [var isLockingFocusWithCustomLensPositionSupported: Bool](avcapturedevice/islockingfocuswithcustomlenspositionsupported.md)
  A Boolean value that indicates whether the device supports locking focus to a specific lens position.
- [var lensPosition: Float](avcapturedevice/lensposition.md)
  The current focus position of the lens.
- [func setFocusModeLocked(lensPosition: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setfocusmodelocked(lensposition:completionhandler:).md)
  Locks the lens position at the specified value, and sets the focus mode to a locked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentlensposition)*