# deviceBrowser(_:deviceDidChangeName:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the name of a device changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeName device: ICDevice)
```

```objc
- (void) deviceBrowser:(ICDeviceBrowser *) browser deviceDidChangeName:(ICDevice *) device;
```

## Discussion

A device’s name may change if a device module overrides the default name reported by the device’s transport layer, or if a user changes the name of the file system volume mounted by the device.

## See Also

### Responding to Device Changes
- [func deviceBrowser(ICDeviceBrowser, requestsSelect: ICDevice)](./devicebrowser%28_,requestsselect%29.md)
  Tells the delegate when an event occurs on the device that may be of interest to the client application.
- [func deviceBrowser(ICDeviceBrowser, deviceDidChangeSharingState: ICDevice)](./devicebrowser%28_,devicedidchangesharingstate%29.md)
  Tells the delegate when the sharing state of a device changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowserdelegate/devicebrowser(_:devicedidchangename:))*