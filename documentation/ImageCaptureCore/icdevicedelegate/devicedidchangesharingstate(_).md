# deviceDidChangeSharingState(_:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the sharing state of a device changes.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: Device sharing is no longer available

## Declaration

```swift
optional func deviceDidChangeSharingState(_ device: ICDevice)
```

```objc
- (void) deviceDidChangeSharingState:(ICDevice *) device;
```

## Discussion

Any Image Capture client application can choose to share the device over the network using the sharing or webSharing facility in Image Capture.

Execution of the delegate callback occurs on the main thread.

## See Also

### Responding to Device Changes
- [func deviceDidChangeName(ICDevice)](./devicedidchangename%28_%29.md)
  Tells the delegate when the name of a device changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicedelegate/devicedidchangesharingstate(_:))*