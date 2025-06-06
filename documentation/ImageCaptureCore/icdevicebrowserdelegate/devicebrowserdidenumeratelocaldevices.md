# deviceBrowserDidEnumerateLocalDevices(_:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the delegate that the device browser has completed sending [`deviceBrowser(_:didAdd:moreComing:)`](icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:).md) for all local devices.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func deviceBrowserDidEnumerateLocalDevices(_ browser: ICDeviceBrowser)
```

#### Discussion

Detecting locally connected devices (USB and FireWire devices) is faster than detecting devices connected using a network protocol. An Image Capture client application may use this message to update its user interface to let the user know that it has completed looking for locally connected devices and then started looking for network devices.

## See Also

- [func deviceBrowser(ICDeviceBrowser, didAdd: ICDevice, moreComing: Bool)](icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:).md)
  Tells the delegate that a device has been added.
- [func deviceBrowser(ICDeviceBrowser, didRemove: ICDevice, moreGoing: Bool)](icdevicebrowserdelegate/devicebrowser(_:didremove:moregoing:).md)
  Tells the delegate that a device has been removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowserdelegate/devicebrowserdidenumeratelocaldevices(_:))*