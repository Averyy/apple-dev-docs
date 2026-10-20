# deviceBrowser(_:deviceDidChangeSharingState:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the sharing state of a device changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.13
- visionOS 1.0+

> **Deprecated**: deviceDidChangeSharingState will no longer be called

## Declaration

```swift
optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeSharingState device: ICDevice)
```

```objc
- (void) deviceBrowser:(ICDeviceBrowser *) browser deviceDidChangeSharingState:(ICDevice *) device;
```

## See Also

### Responding to Device Changes
- [func deviceBrowser(ICDeviceBrowser, requestsSelect: ICDevice)](./devicebrowser%28_,requestsselect%29.md)
  Tells the delegate when an event occurs on the device that may be of interest to the client application.
- [func deviceBrowser(ICDeviceBrowser, deviceDidChangeName: ICDevice)](./devicebrowser%28_,devicedidchangename%29.md)
  Tells the delegate when the name of a device changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowserdelegate/devicebrowser(_:devicedidchangesharingstate:))*