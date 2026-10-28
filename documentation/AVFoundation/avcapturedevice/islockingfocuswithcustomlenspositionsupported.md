# isLockingFocusWithCustomLensPositionSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isLockingFocusWithCustomLensPositionSupported) BOOL lockingFocusWithCustomLensPositionSupported;
```

## Discussion

If this property’s value is [`false`](../../Swift/false.md), calling the [`setFocusModeLocked(lensPosition:completionHandler:)`](./setfocusmodelocked%28lensposition,completionhandler%29.md) method with a lens position value other than [`currentLensPosition`](./currentlensposition.md) raises an exception.

## See Also

### Setting focus manually
- [var lensPosition: Float](./lensposition.md)
  The current focus position of the lens.
- [class let currentLensPosition: Float](./currentlensposition.md)
  A constant that represents the current lens position.
- [func setFocusModeLocked(lensPosition: Float, completionHandler: ((CMTime) -> Void)?)](./setfocusmodelocked%28lensposition,completionhandler%29.md)
  Locks the lens position at the specified value, and sets the focus mode to a locked state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/islockingfocuswithcustomlenspositionsupported)*