# deviceDidChangeSharingState(_:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the delegate when the sharing state of a device changes.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func deviceDidChangeSharingState(_ device: ICDevice)
```

#### Discussion

Any Image Capture client application can choose to share the device over the network using the sharing or webSharing facility in Image Capture.

Execution of the delegate callback occurs on the main thread.

## See Also

- [func deviceDidChangeName(ICDevice)](icdevicedelegate/devicedidchangename(_:).md)
  Tells the delegate when the name of a device changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicedelegate/devicedidchangesharingstate(_:))*