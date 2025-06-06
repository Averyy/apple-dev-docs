# isLockingFocusWithCustomLensPositionSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device supports locking focus to a specific lens position.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLockingFocusWithCustomLensPositionSupported: Bool { get }
```

#### Discussion

If this property’s value is [`false`](https://developer.apple.com/documentation/swift/false), calling the [`setFocusModeLocked(lensPosition:completionHandler:)`](avcapturedevice/setfocusmodelocked(lensposition:completionhandler:).md) method with a lens position value other than [`currentLensPosition`](avcapturedevice/currentlensposition.md) raises an exception.

## See Also

- [var lensPosition: Float](avcapturedevice/lensposition.md)
  The current focus position of the lens.
- [class let currentLensPosition: Float](avcapturedevice/currentlensposition.md)
  A constant that represents the current lens position.
- [func setFocusModeLocked(lensPosition: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setfocusmodelocked(lensposition:completionhandler:).md)
  Locks the lens position at the specified value, and sets the focus mode to a locked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/islockingfocuswithcustomlenspositionsupported)*