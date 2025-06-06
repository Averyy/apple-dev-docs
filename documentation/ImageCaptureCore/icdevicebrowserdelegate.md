# ICDeviceBrowserDelegate

**Framework**: ImageCaptureCore  
**Kind**: protocol

Methods for managing the addition and removal of devices and responding to device changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
protocol ICDeviceBrowserDelegate : NSObjectProtocol
```

## Topics

### Adding and Removing Devices
- [func deviceBrowser(ICDeviceBrowser, didAdd: ICDevice, moreComing: Bool)](icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:).md)
  Tells the delegate that a device has been added.
- [func deviceBrowser(ICDeviceBrowser, didRemove: ICDevice, moreGoing: Bool)](icdevicebrowserdelegate/devicebrowser(_:didremove:moregoing:).md)
  Tells the delegate that a device has been removed.
- [func deviceBrowserDidEnumerateLocalDevices(ICDeviceBrowser)](icdevicebrowserdelegate/devicebrowserdidenumeratelocaldevices(_:).md)
  Tells the delegate that the device browser has completed sending [`deviceBrowser(_:didAdd:moreComing:)`](icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:).md) for all local devices.
### Responding to Device Changes
- [func deviceBrowser(ICDeviceBrowser, requestsSelect: ICDevice)](icdevicebrowserdelegate/devicebrowser(_:requestsselect:).md)
  Tells the delegate when an event occurs on the device that may be of interest to the client application.
- [func deviceBrowser(ICDeviceBrowser, deviceDidChangeName: ICDevice)](icdevicebrowserdelegate/devicebrowser(_:devicedidchangename:).md)
  Tells the delegate when the name of a device changes.
- [func deviceBrowser(ICDeviceBrowser, deviceDidChangeSharingState: ICDevice)](icdevicebrowserdelegate/devicebrowser(_:devicedidchangesharingstate:).md)
  Tells the delegate when the sharing state of a device changes.
### Instance Methods
- [func deviceBrowserDidCancelSuspendOperations(ICDeviceBrowser)](icdevicebrowserdelegate/devicebrowserdidcancelsuspendoperations(_:).md)
- [func deviceBrowserDidResumeOperations(ICDeviceBrowser)](icdevicebrowserdelegate/devicebrowserdidresumeoperations(_:).md)
- [func deviceBrowserDidSuspendOperations(ICDeviceBrowser)](icdevicebrowserdelegate/devicebrowserdidsuspendoperations(_:).md)
- [func deviceBrowserWillSuspendOperations(ICDeviceBrowser)](icdevicebrowserdelegate/devicebrowserwillsuspendoperations(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any ICDeviceBrowserDelegate)?](icdevicebrowser/delegate.md)
  The object that acts as the delegate of the device browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowserdelegate)*