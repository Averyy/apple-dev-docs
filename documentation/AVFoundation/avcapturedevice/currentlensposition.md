# currentLensPosition

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```c
extern const float AVCaptureLensPositionCurrent;
```

## Discussion

Pass this value to the [`setFocusModeLocked(lensPosition:completionHandler:)`](./setfocusmodelocked%28lensposition,completionhandler%29.md) method to lock focus without changing the current lens position.

## See Also

### Setting focus manually
- [var isLockingFocusWithCustomLensPositionSupported: Bool](./islockingfocuswithcustomlenspositionsupported.md)
  A Boolean value that indicates whether the device supports locking focus to a specific lens position.
- [var lensPosition: Float](./lensposition.md)
  The current focus position of the lens.
- [func setFocusModeLocked(lensPosition: Float, completionHandler: ((CMTime) -> Void)?)](./setfocusmodelocked%28lensposition,completionhandler%29.md)
  Locks the lens position at the specified value, and sets the focus mode to a locked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentlensposition)*