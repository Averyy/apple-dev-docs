# ICDeviceBrowserDelegate

**Framework**: ImageCaptureCore  
**Kind**: protocol  
**Role**: Protocol

Methods for managing the addition and removal of devices and responding to device changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
protocol ICDeviceBrowserDelegate : NSObjectProtocol
```

```objc
@protocol ICDeviceBrowserDelegate <NSObject>
```

## Topics

### Adding and Removing Devices
- [func deviceBrowser(ICDeviceBrowser, didAdd: ICDevice, moreComing: Bool)](./icdevicebrowserdelegate/devicebrowser%28_,didadd,morecoming%29.md)
  Tells the delegate that a device has been added.
- [func deviceBrowser(ICDeviceBrowser, didRemove: ICDevice, moreGoing: Bool)](./icdevicebrowserdelegate/devicebrowser%28_,didremove,moregoing%29.md)
  Tells the delegate that a device has been removed.
- [func deviceBrowserDidEnumerateLocalDevices(ICDeviceBrowser)](./icdevicebrowserdelegate/devicebrowserdidenumeratelocaldevices%28_%29.md)
  Tells the delegate that the device browser has completed sending [`deviceBrowser(_:didAdd:moreComing:)`](./icdevicebrowserdelegate/devicebrowser%28_,didadd,morecoming%29.md) for all local devices.
### Responding to Device Changes
- [func deviceBrowser(ICDeviceBrowser, requestsSelect: ICDevice)](./icdevicebrowserdelegate/devicebrowser%28_,requestsselect%29.md)
  Tells the delegate when an event occurs on the device that may be of interest to the client application.
- [func deviceBrowser(ICDeviceBrowser, deviceDidChangeName: ICDevice)](./icdevicebrowserdelegate/devicebrowser%28_,devicedidchangename%29.md)
  Tells the delegate when the name of a device changes.
- [func deviceBrowser(ICDeviceBrowser, deviceDidChangeSharingState: ICDevice)](./icdevicebrowserdelegate/devicebrowser%28_,devicedidchangesharingstate%29.md)
  Tells the delegate when the sharing state of a device changes.
### Instance Methods
- [func deviceBrowserDidCancelSuspendOperations(ICDeviceBrowser)](./icdevicebrowserdelegate/devicebrowserdidcancelsuspendoperations%28_%29.md)
- [func deviceBrowserDidResumeOperations(ICDeviceBrowser)](./icdevicebrowserdelegate/devicebrowserdidresumeoperations%28_%29.md)
- [func deviceBrowserDidSuspendOperations(ICDeviceBrowser)](./icdevicebrowserdelegate/devicebrowserdidsuspendoperations%28_%29.md)
- [func deviceBrowserWillSuspendOperations(ICDeviceBrowser)](./icdevicebrowserdelegate/devicebrowserwillsuspendoperations%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing Device Browsing
- [var delegate: (any ICDeviceBrowserDelegate)?](./icdevicebrowser/delegate.md)
  The object that acts as the delegate of the device browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowserdelegate)*